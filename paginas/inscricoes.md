---
layout: page
permalink: /inscriçao/
title: info.inscricoes

form_MDD:
    br: https://forms.gle/DChjnds564F9cick7
    en: https://forms.gle/DChjnds564F9cick7

form_DFC:
    br: https://forms.gle/8k6wWVkjKt2JeLG36
    en: https://forms.gle/8k6wWVkjKt2JeLG36

---

## {% t inscricoes.regimento %}

| {% t inscricoes.regimento %}: <http://cpg.eel.usp.br/normas_regimento>{: target="_blank"} |
| {% t inscricoes.forms %}: <http://cpg.eel.usp.br/formulario-cpg>{: target="_blank"} |
| {% t inscricoes.editais %}: <http://cpg.eel.usp.br/Editais_Selecao_Abertos>{: target="_blank"} |
{: .table .table-striped .table-hover .table-responsive .table-condensed}

## {% t inscricoes.forms %}

| {% t inscricoes.mestrado_dd %}: <a href="{% if site.lang == 'en' %}{{page.form_MDD.en}}{%else%}{{page.form_MDD.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a> |
| {% t inscricoes.doutorado %}: <a href="{% if site.lang == 'en' %}{{page.form_DFC.en}}{%else%}{{page.form_DFC.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a> |
| {% t inscricoes.alunoespecial %}: {% t inscricoes.foradoar %} |
{: .table .table-striped .table-hover .table-responsive .table-condensed}
