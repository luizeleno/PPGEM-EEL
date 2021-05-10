---
title: global.publicacoes
layout: page
#permalink: /publicacoes/
permalink: /seocacilbup/

---

{% assign fim = 'now' | date: '%Y' %}

{% assign inicio = fim | minus: 5 %}

{% for i in (inicio..fim) reversed %}

{% capture n %}{% bibliography_count --query @*[year={{i}}] %}{% endcapture %}

{% assign n = n | plus: 0 %}
{% if n > 0 %}

#### {{i}}

{% bibliography --query @*[year={{i}}] %}

{% endif %}

{% endfor %}
