---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<p>
  <a class="btn" href="{{ base_path }}/files/cv.pdf" target="_blank" rel="noopener">Download CV (PDF)</a>
  <span class="small">(coming soon)</span>
</p>

Education
======
* Ph.D in Computer Science, University of Technology Sydney, Australia, 2021. Supervised by Prof. Yi Yang.
* B.S. in Electronic and Information Engineering, University of Science and Technology of China, 2018.

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<!-- Talks / Teaching sections intentionally hidden per current content policy -->

Service and leadership
======
* Invited Area Chair (AC), ECCV 2026, CVPR 2026
