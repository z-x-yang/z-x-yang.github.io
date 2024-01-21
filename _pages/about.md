---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
About Me
=======
  I'm currently a postdoctoral researcher in CCAI, college of computer science, at Zhejiang University. My current research interest is computer vision, including multi-modal learning, vision generation, 3D vision, object-centric understanding, etc.


<br />

Education
=======
* Ph.D in Computer Science, University of Technology Sydney, Australia, 2021. Supervised by Prof. Yi Yang.
* B.S. in Electronic and Information Engineering, University of Science and Technology of China, 2018


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