---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  Full publication record: <u><a href="{{author.googlescholar}}" target="_blank" rel="noopener">Google Scholar</a></u>
{% endif %}

{% include base_path %}

<div class="section-jump">
  <a href="#biomed">Translational Biomedical AI</a>
  <a href="#gen">Controllable Multimodal Generation</a>
  <a href="#perception">Multimodal Perception and Understanding</a>
</div>

{% assign sorted_pubs = site.publications | sort: "pub_year" | reverse %}

<h2 id="biomed">Translational Biomedical AI</h2>
<div class="pub-grid">
  {% for post in sorted_pubs %}
    {% if post.topic == "Translational Biomedical AI" %}
      {% include publication-item-ap.html %}
    {% endif %}
  {% endfor %}
</div>

<h2 id="gen">Controllable Multimodal Generation</h2>
<div class="pub-grid">
  {% for post in sorted_pubs %}
    {% if post.topic == "Controllable Multimodal Generation" %}
      {% include publication-item-ap.html %}
    {% endif %}
  {% endfor %}
</div>

<h2 id="perception">Multimodal Perception and Understanding</h2>
<div class="pub-grid">
  {% for post in sorted_pubs %}
    {% if post.topic == "Multimodal Perception and Understanding" %}
      {% include publication-item-ap.html %}
    {% endif %}
  {% endfor %}
</div>
