#!/bin/bash

echo "正在启动Jekyll服务器（简化版本）..."

# 停止任何现有的Jekyll进程
pkill -f jekyll 2>/dev/null || true

# 使用Docker启动Jekyll，使用更简单的配置
echo "启动Docker容器..."
docker run --rm -d \
  --name jekyll-server \
  -p 4000:4000 \
  -v "$(pwd)":/srv/jekyll \
  jekyll/jekyll:latest \
  bash -c "cd /srv/jekyll && bundle install --quiet && jekyll serve --host=0.0.0.0 --port=4000 --force_polling"

# 等待服务器启动
echo "等待服务器启动..."
sleep 30

# 检查容器状态
if docker ps | grep -q jekyll-server; then
    echo "✅ Jekyll服务器已启动！"
    echo "请在浏览器中访问: http://localhost:4000"
    echo ""
    echo "要停止服务器，请运行:"
    echo "docker stop jekyll-server"
else
    echo "❌ 服务器启动失败"
    echo "查看日志:"
    docker logs jekyll-server
fi
