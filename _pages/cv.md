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
</p>

Education
======
* Ph.D in Computer Science, University of Technology Sydney, Australia, 2021. Supervised by Prof. Yi Yang.
* B.E. in Electronic and Information Engineering, University of Science and Technology of China, 2018.

Employment
======
* ZJU100 Young Professor, College of Artificial Intelligence, Zhejiang University, 2026–present.
* Research Fellow, Department of Biomedical Informatics (DBMI), Harvard Medical School, Harvard University, 2024–2026.
* Postdoctoral Researcher, CCAI, Zhejiang University, 2021–2024.
* Research Intern, Baidu Research, 2019–2021.

Publications
======
{% assign sorted_pubs = site.publications | sort: "pub_year" | reverse %}
  <ul>{% for post in sorted_pubs %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<!-- Talks / Teaching sections intentionally hidden per current content policy -->

Service and leadership
======
* Invited Area Chair, ICLR 2027; Senior Program Committee Member, AAAI 2027; Area Chair, ECCV 2026; Outstanding Area Chair, CVPR 2026
* Workshop Organizer, Pixel-level Video Understanding in the Wild Challenge at CVPR 2023–2026
