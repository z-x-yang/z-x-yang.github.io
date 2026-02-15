---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Research Fellow in the Department of Biomedical Informatics (DBMI) at Harvard Medical School, Harvard University, working with Prof. Tianxi Cai.
Previously, I was a postdoctoral researcher at CCAI, College of Computer Science and Technology, Zhejiang University (2021–2024), advised by Prof. Yi Yang.
My research builds reliable and controllable multimodal learning and generation methods, with growing emphasis on translational biomedical applications.

{% assign selected = site.publications | where: "selected", true | sort: "pub_year" | reverse %}

My work is organized around three connected research directions:

<div class="research-track">
  <h3>1) Translational Biomedical AI</h3>
  <p>Building biology-informed and clinically grounded AI systems across medical imaging, EHR intelligence, and translational biomedical settings.</p>
</div>

<div class="research-track">
  <h3>2) Controllable Multimodal Generation</h3>
  <p>Developing controllable multimodal generation methods for image, video, and 3D content, with emphasis on compositionality, reliability, and practical usability.</p>
</div>

<div class="research-track">
  <h3>3) Multimodal Perception and Understanding</h3>
  <p>Advancing multimodal perception and understanding for dynamic environments through segmentation, tracking, and reasoning with robust temporal consistency.</p>
</div>

<p class="section-jump">
  <a href="{{ base_path }}/research/">Research overview</a>
  <a href="{{ base_path }}/publications/">Full publications</a>
</p>

<br />

{% include updates.html limit=5 %}

<br />

## Selected Publications

{% assign catr_title = "CATR: Combinatorial-Dependence Audio-Queried Transformer for Audio-Visual Video Segmentation" %}
{% assign catr_pub = selected | where: "title", catr_title | first %}

<div class="pub-grid">
{% if catr_pub %}
  {% assign post = catr_pub %}
  {% include publication-item-ap.html %}
{% endif %}

{% assign shown = 0 %}
{% if catr_pub %}
  {% assign regular_limit = 11 %}
{% else %}
  {% assign regular_limit = 12 %}
{% endif %}

{% for post in selected %}
  {% if post.title != catr_title %}
    {% include publication-item-ap.html %}
    {% assign shown = shown | plus: 1 %}
    {% if shown >= regular_limit %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</div>

<p><a href="{{ base_path }}/publications/">See full publication list →</a></p>

<br />

## Selected Awards
{% include base_path %}

{% for post in site.awards reversed %}
  {% include archive-single.html %}
{% endfor %}
