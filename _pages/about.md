---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% include base_path %}

I'm currently a postdoctoral researcher of computer science at Zhejiang University. My current research interest is computer vision, including video understanding, visual generation, and metric learning.



Education
======
* B.S. in Electronic and Information Engineering, University of Science and Technology of China, 2018
* Ph.D in Computer Science, University of Technology Sydney, Australia, 2021


Publications
=======
 <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Awards
=======
 <ul>{% for post in site.awards %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>