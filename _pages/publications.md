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
{% assign sorted_pubs = site.publications | sort: "pub_year" | reverse %}
{% assign biomed_all = sorted_pubs | where: "topic", "Translational Biomedical AI" %}
{% assign gen_all = sorted_pubs | where: "topic", "Controllable Multimodal Generation" %}
{% assign perception_all = sorted_pubs | where: "topic", "Multimodal Perception and Understanding" %}
{% assign biomed_selected = biomed_all | where: "selected", true %}
{% assign gen_selected = gen_all | where: "selected", true %}
{% assign perception_selected = perception_all | where: "selected", true %}

<div class="section-jump">
  <a href="#biomed">Translational Biomedical AI</a>
  <a href="#gen">Controllable Multimodal Generation</a>
  <a href="#perception">Multimodal Perception and Understanding</a>
</div>

<div class="track-block" id="biomed">
  <h2>Translational Biomedical AI</h2>
  <p class="track-meta">Selected {{ biomed_selected | size }} / Total {{ biomed_all | size }}</p>
  <div class="pub-grid">
    {% for post in biomed_selected %}
      {% include publication-item-ap.html %}
    {% endfor %}
  </div>
  <details>
    <summary>Show full list ({{ biomed_all | size }} papers)</summary>
    <div class="pub-grid">
      {% for post in biomed_all %}
        {% include publication-item-ap.html %}
      {% endfor %}
    </div>
  </details>
</div>

<div class="track-block" id="gen">
  <h2>Controllable Multimodal Generation</h2>
  <p class="track-meta">Selected {{ gen_selected | size }} / Total {{ gen_all | size }}</p>
  <div class="pub-grid">
    {% for post in gen_selected %}
      {% include publication-item-ap.html %}
    {% endfor %}
  </div>
  <details>
    <summary>Show full list ({{ gen_all | size }} papers)</summary>
    <div class="pub-grid">
      {% for post in gen_all %}
        {% include publication-item-ap.html %}
      {% endfor %}
    </div>
  </details>
</div>

<div class="track-block" id="perception">
  <h2>Multimodal Perception and Understanding</h2>
  <p class="track-meta">Selected {{ perception_selected | size }} / Total {{ perception_all | size }}</p>
  <div class="pub-grid">
    {% for post in perception_selected %}
      {% include publication-item-ap.html %}
    {% endfor %}
  </div>
  <details>
    <summary>Show full list ({{ perception_all | size }} papers)</summary>
    <div class="pub-grid">
      {% for post in perception_all %}
        {% include publication-item-ap.html %}
      {% endfor %}
    </div>
  </details>
</div>
