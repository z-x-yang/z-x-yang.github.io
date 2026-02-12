---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Postdoctoral Researcher at Harvard University, working on reliable and controllable AI systems for high-impact real-world use.

My work is organized around three connected research directions:

<div class="research-track">
  <h3>1) Translational Biomedical AI</h3>
  <p>Building clinically useful AI systems across medical imaging, EHR intelligence, and next-generation biomedical data modalities.</p>
</div>

<div class="research-track">
  <h3>2) Controllable Multimodal Generation</h3>
  <p>Developing controllable generative models for image/video/3D content creation with strong compositionality and reliability.</p>
</div>

<div class="research-track">
  <h3>3) Multimodal Perception and Understanding</h3>
  <p>Advancing dynamic scene understanding through segmentation, tracking, and multimodal reasoning in complex environments.</p>
</div>

<br />

{% include updates.html limit=5 %}

<br />

## Selected Publications

{% assign selected = site.publications | where: "selected", true | sort: "pub_year" | reverse %}
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
