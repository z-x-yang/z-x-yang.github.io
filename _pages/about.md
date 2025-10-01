---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
About
=====
  I am a postdoctoral researcher focused on building reliable AI systems for the real world. My research spans two complementary tracks:
  
  - Multimodal Generation and Understanding: advancing generative modeling and multimodal alignment across 3D, video, and audio, with an emphasis on controllability, robustness, and data efficiency.
  - Biomedical AI (Medical Imaging & EHR): developing methods for medical image segmentation/understanding and electronic health record analysis, toward interpretable, transferable clinical intelligence.

<br />

{% include updates.html limit=5 %}

<br />

Selected Publications
=======
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

<br />

Selected Awards
=======
{% include base_path %}

{% for post in site.awards reversed %}
  {% include archive-single.html %}
{% endfor %}