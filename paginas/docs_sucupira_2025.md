---
layout: page
permalink: /sucupira2025/
title: sucupira.titulo
---

{% contentfor br %}
Segue a lista de documentos comprobatórios atestando as atividades realizadas pelos docentes do programa ao longo do período avaliativo:
{% endcontentfor %}

{% contentfor en %}
Below is a list of supporting documents attesting to the activities carried out by the program's members throughout the evaluation period:
{% endcontentfor %}

<div id="treatments" class="treatments">
    <div class="container-fluid">
        <div class="row">
            {% for doc in (1..12) %}
                <div class="col-sm-6 col-md-4" >
                    <div class="icon-box" style="text-align: center;">
                        <p><a class="btn btn-lg btn-primary my-1" href="/assets/DOCS_FISICOS/Doc{{doc}}.pdf" target="_blank">Documento {{doc}}</a></p>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</div>
