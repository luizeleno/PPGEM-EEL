---
layout: page
permalink: /inscricao/
title: info.inscricoes

form_MDD:
    br: https://inscricao.eel.usp.br/  # https://ppgem-inscricao.eel.usp.br/pt-br/inscricao
    en: https://inscricao.eel.usp.br/  # https://ppgem-inscricao.eel.usp.br/pt-br/inscricao

form_DFC:
    br: https://inscricao.eel.usp.br/  # https://forms.gle/2itVt3G3RCxw21y86
    en: https://inscricao.eel.usp.br/  # https://forms.gle/2itVt3G3RCxw21y86

form_AE:
    br: https://inscricao.eel.usp.br/  # https://www.ppgem-inscricao.eel.usp.br/pt-br/inscricao-aluno-especial
    en: https://inscricao.eel.usp.br/ # https://www.ppgem-inscricao.eel.usp.br/pt-br/inscricao-aluno-especial

M_DD_open: true # quando inscrição para M/DD estiver aberta
M_especial: true # quando inscrição para aluno especial estiver aberta

# quando estiver fora do ar:
#| {% t inscricoes.alunoespecial %}: {% t inscricoes.foradoar %} |

---

## {% t inscricoes.regimento %}

| {% t inscricoes.regimento %}: <https://cpg.eel.usp.br/apoio-administrativo/regimentos-regulamentos-e-outras-normas>{: target="_blank"} |
| {% t inscricoes.forms %}: <https://cpg.eel.usp.br/apoio-administrativo/formularios>{: target="_blank"} |
| {% t inscricoes.editais %}: <https://cpg.eel.usp.br/apoio-administrativo/editais-de-selecao>{: target="_blank"} |
{: .table .table-striped .table-hover .table-responsive .table-condensed}

## {% t inscricoes.forms %}

| {% t inscricoes.mestrado_dd %}: {% if page.M_DD_open %}<a href="{% if site.lang == 'en' %}{{page.form_MDD.en}}{%else%}{{page.form_MDD.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a>{% else %}{% t inscricoes.foradoar %}{% endif %} |
| {% t inscricoes.doutorado %}: <a href="{% if site.lang == 'en' %}{{page.form_DFC.en}}{%else%}{{page.form_DFC.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a> |
| {% t inscricoes.alunoespecial %}: {% if page.M_especial %}<a href="{% if site.lang == 'en' %}{{page.form_AE.en}}{%else%}{{page.form_AE.br}}{%endif%}" target="_blank">{% t inscricoes.inscricao %}</a>{% else %}{% t inscricoes.foradoar %}{% endif %} |
{: .table .table-striped .table-hover .table-responsive .table-condensed}

## {% t academico.titulo %}

| {% t academico.EEL %} [(PDF)]({{site.baseurl}}/../../assets/proj_acad/PA-EEL.pdf){: target="_blank"}|
| {% t academico.DEMAR %} [(PDF)]({{site.baseurl}}/../../assets/proj_acad/PA-Demar.pdf){: target="_blank"}|
{: .table .table-striped .table-hover .table-responsive .table-condensed}

## {% t outros_docs.titulo %}

| {% t outros_docs.acumulo %}: [Deliberação 064/2023]({{site.baseurl}}/assets/portarias/Deliberação_064_2023.pdf){: target="_blank" .btn .btn-sm .btn-primary} [MEMO 060/2023]({{site.baseurl}}/assets/portarias/MEMO PPGEM 060-2023-AssCS.pdf){: target="_blank" .btn .btn-sm .btn-primary} |
{: .table .table-striped .table-hover .table-responsive .table-condensed}
