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
  I am presently a postdoctoral researcher at Harvard University. My research interests include artificial intelligence, with a focus on multi-modal learning, generative models, 3D vision, and their applications in biomedical fields.


<br />

Education
=======
* Ph.D in Computer Science, University of Technology Sydney, Australia, 2021. Supervised by Prof. Yi Yang.
* B.S. in Electronic and Information Engineering, University of Science and Technology of China, China, 2018.


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