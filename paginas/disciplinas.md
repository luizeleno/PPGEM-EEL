---
layout: page
permalink: /disciplinas/
title: info.disciplinas
---

{% for disc in site.data.disciplinas %}
- {{disc.sigla}} &mdash; {% if site.lang=='br' %}{{ disc.nome_br }}{% else %}{{ disc.nome_en }}{% endif %}
{% endfor %}