---
permalink: /defesas/

---

{% assign teses = site.data.teses | sort: 'data' | reverse %}
{% assign dissertacoes = site.data.dissertacoes | sort: 'data' | reverse %}

 <div class="container-fluid" style="margin-bottom:10px">

<h1>{% t defesas.nav %}</h1>

<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#Doutorado">
  {% t defesas.doutorado %}
</button>

<!-- Modal -->
<div class="modal fade" id="Doutorado" tabindex="-1" aria-labelledby="DoutoradoLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="DoutoradoLabel">{% t defesas.doutorado %}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <table class="table table-condensed table-striped table-hover table-responsive" style="width:100%">
    <colgroup>
       <col span="1" style="width: 49%;">
       <col span="1" style="width: 19%;">
       <col span="1" style="width: 19%;">
       <col span="1" style="width: 13%;">
    </colgroup>
<tr>
    <th>{% t defesas.titulo %}</th>
    <th>{% t defesas.aluno %}</th> 
    <th>{% t defesas.orientador %}</th>
    <th>{% t defesas.data %}</th>
  </tr>
{% for tese in teses %}
<tr>
<td>
{{tese.titulo}}
</td>
<td>
{{tese.aluno}}
</td>
<td>
{{tese.orientador}}
</td>
<td>
{% if site.lang == 'en' %}
    {{ tese.data | date: '%m/%d/%Y' }}{% if tese.horario %}, {{tese.horario}}{% endif %}
{% else %}
    {{ tese.data | date: '%d/%m/%Y' }}{% if tese.horario %}, {{tese.horario}}{% endif %}
{% endif %}
</td>
</tr>
{% endfor %}
</table>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">{% t global.fechar %}</button>
      </div>
    </div>
  </div>
</div>

<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#Mestrado">
  {% t defesas.mestrado %}
</button>

<!-- Modal -->
<div class="modal fade" id="Mestrado" tabindex="-1" aria-labelledby="MestradoLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="MestradoLabel">{% t defesas.mestrado %}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <table class="table table-condensed table-striped table-hover table-responsive" style="width:100%">
    <colgroup>
       <col span="1" style="width: 49%;">
       <col span="1" style="width: 19%;">
       <col span="1" style="width: 19%;">
       <col span="1" style="width: 13%;">
    </colgroup>
<tr>
    <th>{% t defesas.titulo %}</th>
    <th>{% t defesas.aluno %}</th> 
    <th>{% t defesas.orientador %}</th>
    <th>{% t defesas.data %}</th>
  </tr>
{% for tese in dissertacoes %}
<tr>
<td>
{{tese.titulo}}
</td>
<td>
{{tese.aluno}}
</td>
<td>
{{tese.orientador}}
</td>
<td>
{% if site.lang == 'en' %}
    {{ tese.data | date: '%m/%d/%Y' }}{% if tese.horario %}, {{tese.horario}}{% endif %}
{% else %}
    {{ tese.data | date: '%d/%m/%Y' }}{% if tese.horario %}, {{tese.horario}}{% endif %}
{% endif %}
</td>
</tr>
{% endfor %}
</table>

      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">{% t global.fechar %}</button>
      </div>
    </div>
  </div>
</div>


</div>
