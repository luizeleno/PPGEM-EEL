---
title: global.publicacoes
layout: page
permalink: /publicacoes/

start: 1990

---

{% assign inicio = page.start | plus: 0 %}
{% assign fim = 'now' | date: '%Y' %}

{% for i in (inicio..fim) reversed %}

{% capture n %}{% bibliography_count --query @*[year={{i}}] %}{% endcapture %}

{% assign n = n | plus: 0 %}
{% if n > 0 %}

#### {{i}}

{% bibliography --query @*[year={{i}}] %}

{% endif %}

{% endfor %}
