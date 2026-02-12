#!/usr/bin/env bash
# Robust local preview build for AP homepage workflow.
# - Retries build automatically
# - Falls back to minimal config if preview config fails

set -u

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$ROOT_DIR/.build-logs"
OUT_DIR="$ROOT_DIR/_site_preview"
mkdir -p "$LOG_DIR"

export PATH="/opt/homebrew/opt/ruby@3.2/bin:$PATH"
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"

FULL_CONFIG="_config.yml,_config.dev.yml,_config.preview.yml"
FALLBACK_CONFIG="_config.yml,_config.dev.yml"

run_build() {
  local cfg="$1"
  local tag="$2"
  local log="$LOG_DIR/jekyll-build-${tag}-$(date +%Y%m%d-%H%M%S).log"
  echo "[build] config=$cfg"
  bundle exec jekyll build \
    --source "$ROOT_DIR" \
    --destination "$OUT_DIR" \
    --config "$cfg" >"$log" 2>&1
  local code=$?
  if [ $code -eq 0 ]; then
    echo "[ok] build success ($tag)"
    echo "[log] $log"
    return 0
  fi
  echo "[warn] build failed ($tag), exit=$code"
  echo "[log] $log"
  return $code
}

cd "$ROOT_DIR" || exit 1

echo "[step] bundle check"
if ! bundle check >/dev/null 2>&1; then
  echo "[step] bundle install"
  bundle install || true
fi

echo "[step] metadata audit"
python3 tools/publications/normalize_metadata.py --check || true
python3 tools/publications/audit_metadata.py || true

# Try full build up to 2 times
if run_build "$FULL_CONFIG" "full-attempt1"; then
  exit 0
fi

if run_build "$FULL_CONFIG" "full-attempt2"; then
  exit 0
fi

# Fallback path
if run_build "$FALLBACK_CONFIG" "fallback"; then
  echo "[note] fallback config used. Check _config.preview.yml or related plugins."
  exit 0
fi

echo "[error] all build attempts failed. See logs under: $LOG_DIR"
exit 1
