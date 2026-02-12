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

{% assign total_pubs = site.publications | size %}
{% assign selected = site.publications | where: "selected", true | sort: "pub_year" | reverse %}
{% assign biomed = site.publications | where: "topic", "Translational Biomedical AI" %}
{% assign gen = site.publications | where: "topic", "Controllable Multimodal Generation" %}
{% assign perception = site.publications | where: "topic", "Multimodal Perception and Understanding" %}

<div class="hero-stats">
  <span>{{ total_pubs }} Publications</span>
  <span>{{ selected | size }} Selected Highlights</span>
  <span>3 Research Tracks</span>
</div>

My work is organized around three connected research directions:

<div class="research-track">
  <h3>1) Translational Biomedical AI</h3>
  <p>Building clinically useful AI systems across medical imaging, EHR intelligence, and next-generation biomedical data modalities.</p>
  <p class="track-meta">{{ biomed | size }} papers</p>
</div>

<div class="research-track">
  <h3>2) Controllable Multimodal Generation</h3>
  <p>Developing controllable generative models for image/video/3D content creation with strong compositionality and reliability.</p>
  <p class="track-meta">{{ gen | size }} papers</p>
</div>

<div class="research-track">
  <h3>3) Multimodal Perception and Understanding</h3>
  <p>Advancing dynamic scene understanding through segmentation, tracking, and multimodal reasoning in complex environments.</p>
  <p class="track-meta">{{ perception | size }} papers</p>
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
