---
layout: page
permalink: /disciplinas/
title: info.disciplinas
---

{% for disc in site.disciplinas %}
- <a href="{{site.baseurl}}{{disc.url}}">{{disc.sigla}} &mdash; {% if site.lang=='br' %}{{ disc.title }}{% else %}{{ disc.title_en }}{% endif %}</a>
{% endfor %}