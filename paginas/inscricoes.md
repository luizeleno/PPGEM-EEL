---
layout: page
permalink: /inscricoes/
title: info.inscricoes

form:
    br: https://forms.gle/dkMWysAPvkQauF5w9
    en: https://forms.gle/wuFcdfuHwdSyDBRo9

---

- {% t inscricoes.regimento %}: <http://cpg.eel.usp.br/normas_regimento>{: target="_blank"}

- {% t inscricoes.forms %}: <http://cpg.eel.usp.br/formulario-cpg>{: target="_blank"}

- {% t inscricoes.editais %}: <http://cpg.eel.usp.br/Editais_Selecao_Abertos>{: target="_blank"}

- {% t inscricoes.doutorado %}: <a href="{% if site.lang == 'en' %}{{page.form.en}}{%else%}{{page.form.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a>

- {% t inscricoes.alunoespecial %}: {% t inscricoes.foradoar%}