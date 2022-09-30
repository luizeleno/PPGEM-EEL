---
title: global.publicacoes
layout: page
permalink: /publicacoes/
---

{% if site.lang == 'en' %}
***Obs.:*** Listed below are all publications of the program's permanent faculty. Recent publications organized by faculty are listed on their respective personal pages, accessible through the [Faculty list]({{site.baseurl}}/docentes/).
{% else %}
***Obs.:*** Estão listadas abaixo todas as publicações dos docentes permanentes do programa. As publicações recentes separadas por docente permanente estão listadas em suas respectivas páginas pessoais, acessíveis na [Lista de Docentes]({{site.baseurl}}/docentes/).
{% endif %}

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
