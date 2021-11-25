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
I'm currently a postdoctoral researcher of computer science at Zhejiang University. My current research interest is computer vision, including video understanding, visual generation, and metric learning.



Education
=======
* Ph.D in Computer Science, University of Technology Sydney, Australia, 2021
* B.S. in Electronic and Information Engineering, University of Science and Technology of China, 2018



Publications
=======
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

Awards
=======
{% include base_path %}

{% for post in site.awards reversed %}
  {% include archive-single.html %}
{% endfor %}