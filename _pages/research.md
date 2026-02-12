---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}
{% assign sorted_pubs = site.publications | sort: "pub_year" | reverse %}

## Research Agenda (2026–2030)
- Build clinically reliable AI systems that integrate imaging, EHR, and emerging biomedical modalities (e.g., single-cell) for decision support and translational impact.
- Develop controllable multimodal generative models as compositional tools for simulation, synthesis, and hypothesis-driven data generation.
- Advance multimodal perception and understanding in dynamic environments, with emphasis on temporal robustness and scalable deployment.

I view these three tracks as one connected agenda: stronger perception improves controllability, and controllable models accelerate translational biomedical applications.

## Translational Biomedical AI
I focus on translational AI systems that bridge methodological advances and deployable clinical value, including medical imaging foundation models, EHR intelligence, and scalable biomedical data understanding (including emerging modalities such as single-cell data).

<div class="pub-grid">
  {% assign shown = 0 %}
  {% for post in sorted_pubs %}
    {% if post.topic == "Translational Biomedical AI" and post.selected == true and shown < 4 %}
      {% include publication-item-ap.html %}
      {% assign shown = shown | plus: 1 %}
    {% endif %}
  {% endfor %}
</div>

## Controllable Multimodal Generation
I develop controllable multimodal generation methods for image/video/3D creation, with emphasis on compositionality, attribute-level control, and robust behavior under realistic user constraints.

<div class="pub-grid">
  {% assign shown = 0 %}
  {% for post in sorted_pubs %}
    {% if post.topic == "Controllable Multimodal Generation" and post.selected == true and shown < 5 %}
      {% include publication-item-ap.html %}
      {% assign shown = shown | plus: 1 %}
    {% endif %}
  {% endfor %}
</div>

## Multimodal Perception and Understanding
I study scene understanding in dynamic environments through segmentation, tracking, and multimodal reasoning, aiming to improve robustness, temporal consistency, and transferability.

<div class="pub-grid">
  {% assign shown = 0 %}
  {% for post in sorted_pubs %}
    {% if post.topic == "Multimodal Perception and Understanding" and post.selected == true and shown < 5 %}
      {% include publication-item-ap.html %}
      {% assign shown = shown | plus: 1 %}
    {% endif %}
  {% endfor %}
</div>

### Collaboration
I welcome collaborations on clinically grounded AI, controllable multimodal generation, and robust scene understanding. If your interests align, feel free to reach out by email.

<p><a href="{{ base_path }}/publications/">View all publications by track →</a></p>
