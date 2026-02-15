---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Postdoctoral Researcher at Harvard University, increasingly focused on biomedical AI.
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

<div class="pub-grid">
{% for post in selected limit: 12 %}
  {% include publication-item-ap.html %}
{% endfor %}
</div>

<p><a href="{{ base_path }}/publications/">See full publication list →</a></p>

<br />

## Selected Awards
{% include base_path %}

{% for post in site.awards reversed %}
  {% include archive-single.html %}
{% endfor %}
