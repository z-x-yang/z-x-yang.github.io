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
  I'm currently a postdoctoral researcher in computer science at Zhejiang University. My current research interest is computer vision, including vision (image/video/3D) generation, 3D/4D (3D/3D+video) vision, object-centric perception/reconstruction/reasoning, cross-modal learning, etc.


<br />

Education
=======
* Ph.D in Computer Science, University of Technology Sydney, Australia, 2021
* B.S. in Electronic and Information Engineering, University of Science and Technology of China, 2018


<br />

Publications
=======
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

<br />

Awards
=======
{% include base_path %}

{% for post in site.awards reversed %}
  {% include archive-single.html %}
{% endfor %}