---
layout: page
permalink: /inscricao/
title: info.inscricoes

form_MDD:
    br: https://forms.gle/DChjnds564F9cick7
    en: https://forms.gle/DChjnds564F9cick7

form_DFC:
    br: https://forms.gle/8k6wWVkjKt2JeLG36
    en: https://forms.gle/8k6wWVkjKt2JeLG36

form_AE:
    br: https://ppgem-inscricao.eel.usp.br/pt-br/inscricao-aluno-especial
    en: https://ppgem-inscricao.eel.usp.br/pt-br/inscricao-aluno-especial

# quando estiver fora do ar:
#| {% t inscricoes.alunoespecial %}: {% t inscricoes.foradoar %} |

---

## {% t inscricoes.regimento %}

| {% t inscricoes.regimento %}: <http://cpg.eel.usp.br/normas_regimento>{: target="_blank"} |
| {% t inscricoes.forms %}: <http://cpg.eel.usp.br/formulario-cpg>{: target="_blank"} |
| {% t inscricoes.editais %}: <http://cpg.eel.usp.br/Editais_Selecao_Abertos>{: target="_blank"} |
{: .table .table-striped .table-hover .table-responsive .table-condensed}

## {% t inscricoes.forms %}

| {% t inscricoes.mestrado_dd %}: <a href="{% if site.lang == 'en' %}{{page.form_MDD.en}}{%else%}{{page.form_MDD.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a> |
| {% t inscricoes.doutorado %}: <a href="{% if site.lang == 'en' %}{{page.form_DFC.en}}{%else%}{{page.form_DFC.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a> |
| {% t inscricoes.alunoespecial %}: <a href="{% if site.lang == 'en' %}{{page.form_AE.en}}{%else%}{{page.form_AE.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a> |
{: .table .table-striped .table-hover .table-responsive .table-condensed}
