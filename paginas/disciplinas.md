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
    pae:
        br: "97499 - Escola de Engenharia de Lorena"
        en: "97499 - Lorena School of Engineering"

---

{% assign mag = site.disciplinas | where:'area.br', page.area.mag.br %}
{% assign mat = site.disciplinas | where:'area.br', page.area.mat.br %}
{% assign pae = site.disciplinas | where:'area.br', page.area.pae.br %}

<table class="table table-striped table-hover table-responsive table-condensed" style="width:100%">
        <tr>
<!--             não há mais áreas diferentes, então segue um hack pra eliminá-las -->
<!--             <th>{%if site.lang=='en'%}{{page.area.mat.en}}{%else%}{{page.area.mat.br}}{%endif%}</th> -->
<!--             <th>{%if site.lang=='en'%}{{page.area.mag.en}}{%else%}{{page.area.mag.br}}{%endif%}</th> -->
            <th></th>
            <th></th>
        </tr>
        <tr>
            <td>
                {% for disc in mat %}
                        <p><a href="{{site.baseurl}}{{disc.url}}">{{disc.sigla}} &ndash; {% if site.lang=='br' %}{{ disc.title }}{% else %}{{ disc.title_en }}{% endif %}</a></p>
                {% endfor %}
            </td>
            <td>
                {% for disc in mag %}
                    <p><a href="{{site.baseurl}}{{disc.url}}">{{disc.sigla}} &ndash; {% if site.lang=='br' %}{{ disc.title }}{% else %}{{ disc.title_en }}{% endif %}</a></p>
                {% endfor %}

                <table class="table table-striped table-hover table-responsive table-condensed" style="width:100%">
                    <tr>
<!--                      não há mais áreas diferentes, então segue um hack pra eliminá-las -->
<!--                     <th>{%if site.lang=='en'%}{{page.area.pae.en}}{%else%}{{page.area.pae.br}}{%endif%}</th> -->
                    <th></th>
                    </tr>
                    <tr>
                        <td>
                            {% for disc in pae %}
                                <p><a href="{{site.baseurl}}{{disc.url}}">{{disc.sigla}} &ndash; {% if site.lang=='br' %}{{ disc.title }}{% else %}{{ disc.title_en }}{% endif %}</a></p>
                            {% endfor %}
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
