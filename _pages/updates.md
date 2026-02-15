---
layout: single
title: "Updates"
permalink: /updates/
author_profile: true
---

{% include base_path %}

<h1>Updates</h1>

<ul>
{% assign items = site.data.updates | reverse %}
{% for u in items %}
  <li>
    <strong>{{ u.date }}</strong>: {{ u.text }}
    {% if u.link %}
      <a class="updates__source-link" href="{{ u.link }}" target="_blank" rel="noopener">(source)</a>
    {% endif %}
  </li>
{% endfor %}
</ul>


