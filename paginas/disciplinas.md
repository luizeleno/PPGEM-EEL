---
layout: page
permalink: /disciplinas/
title: info.disciplinas

area:
    mag:
        br: "97135 - Magnetismo e Supercondutividade"
        en: "97135 - Magnetism and Superconductivity"
    mat:
        br: "97134 - Materiais Convencionais e Avançados"
        en: "97135 - Conventional and Advanced Materials"
---

{% assign mag = site.disciplinas | where:'area.br', page.area.mag.br %}
{% assign mat = site.disciplinas | where:'area.br', page.area.mat.br %}

<table class="table table-striped table-hover table-responsive table-condensed" style="width:100%">
        <tr>
            <th>{%if site.lang=='en'%}{{page.area.mat.en}}{%else%}{{page.area.mat.br}}{%endif%}</th>
            <th>{%if site.lang=='en'%}{{page.area.mag.en}}{%else%}{{page.area.mag.br}}{%endif%}</th>
        </tr>
        <tr>
            <td>
                <ul>
                    {% for disc in mat %}
                        <li>
                            <a href="{{site.baseurl}}{{disc.url}}">{{disc.sigla}} &mdash; {% if site.lang=='br' %}{{ disc.title }}{% else %}{{ disc.title_en }}{% endif %}</a>
                        </li>
                    {% endfor %}
                </ul>
            </td>
            <td>
                <ul>
                    {% for disc in mag %}
                        <li>
                            <a href="{{site.baseurl}}{{disc.url}}">{{disc.sigla}} &mdash; {% if site.lang=='br' %}{{ disc.title }}{% else %}{{ disc.title_en }}{% endif %}</a>
                        </li>
                    {% endfor %}
                </ul>
            </td>
        </tr>
    </table>
