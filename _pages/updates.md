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
    <strong>{{ u.date }}</strong>: 
    {% if u.link %}
      <a href="{{ u.link }}">{{ u.text }}</a>
    {% else %}
      {{ u.text }}
    {% endif %}
  </li>
{% endfor %}
</ul>


