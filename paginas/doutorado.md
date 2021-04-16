---
title: inscricoes.doutorado
layout: page
permalink: /doutorado/
---

<div class="form">
    <h4>Dados pessoais</h4>
    <form method="POST" action="" id="doutorado">
        <div class="form-field">
            <label class="form-label">Nome*</label>
            <input name="Nome" type="text" placeholder="Nome*" required>
        </div>
        <div class="row form-field">
            <div class="col-sm-6">
                <label class="form-label">E-mail*</label>
                <input name="Email" type="email" placeholder="E-mail*" required>
            </div>
            <div class="col-sm-6">
                <label class="form-label">Número USP*</label>
                <input name="NUSP" type="text" placeholder="Número USP">
            </div>
        </div>
        <div class="row form-field">
            <div class="col-sm-3">
                <label class="form-label">CPF</label>
                <input name="CPF" type="text" placeholder="CPF*" required>
            </div>
            <div class="col-sm-3">
                <label class="form-label">RG*</label>
                <input name="RG" type="text" placeholder="RG*" required>
            </div>
            <div class="col-sm-3">
                <label class="form-label">Data de emissão*</label>
                <input name="Emissao" type="text" placeholder="Data de emissão* (dd/mm/aaaa)" required>
            </div>
            <div class="col-sm-3">
                <label class="form-label">Órgão emissor*</label>
                <input name="Orgao" type="text" placeholder="Órgão emissor*" required>
            </div>
        </div>
        <div class="row form-field">
            <div class="col-sm-4">
                <input name="PISPASEP" type="text" placeholder="PIS/PASEP*" required>
            </div>
            <div class="col-sm-4">
                <input name="Nascimento" type="text" placeholder="Data de nascimento* (dd/mm/aaaa)" required>
            </div>
            <div class="col-sm-4">
                <input name="Telefone" type="text" placeholder="Telefone*" required>
            </div>
        </div>
        <div class="row form-field">
            <div class="col-sm-6">
                <input name="Endereco" type="text" placeholder="Endereço*" required>
            </div>
            <div class="col-sm-6">
                <input name="Bairro" type="text" placeholder="Bairro*" required>
            </div>
        </div>
        <div class="row form-field">
            <div class="col-sm-4">
                <input name="CEP" type="text" placeholder="CEP*" required>
            </div>
            <div class="col-sm-4">
                <input name="Cidade" type="text" placeholder="Cidade*" required>
            </div>
            <div class="col-sm-4">
                <input name="Estado" type="text" placeholder="Estado/País*" required>
            </div>
        </div>
        <h4>Dados bancários</h4>
        <div class="row form-field">
            <div class="col-sm-4">
                <input name="Banco" type="text" placeholder="Banco*" required>
            </div>
            <div class="col-sm-4">
                <input name="Agência" type="text" placeholder="Agência*" required>
            </div>
            <div class="col-sm-4">
                <input name="Conta" type="text" placeholder="Conta corrente*" required>
            </div>
        </div>
        <h4>Formação</h4>
         <div class="form-field">
            <input name="Titulo" type="text" placeholder="Título*" required>
        </div>
         <div class="form-field">
            <input name="Instituicao" type="text" placeholder="Instituiçao*" required>
        </div>
         <div class="form-field">
            <input name="Programa" type="text" placeholder="Doutor/mestre em*" required>
        </div>
        <div class="row form-field">
            <div class="col-sm-4">
                <input name="Area" type="text" placeholder="Área de formação*" required>
            </div>
            <div class="col-sm-4">
                <input name="Inicio" type="text" placeholder="Data de início* (dd/mm/aaaa)" required>
            </div>
            <div class="col-sm-4">
                <input name="Termino" type="text" placeholder="Data de término (dd/mm/aaaa)*" required>
            </div>
        </div>
         <div class="form-field">
            <input name="Orientador" type="text" placeholder="Orientador*" required>
        </div>
        <h4>Dados profissionais</h4>
         <div class="form-field">
            <input name="TipoEmpregador" type="text" placeholder="Tipo de empregador*" required>
        </div>
         <div class="form-field">
            <input name="Empregador" type="text" placeholder="Empregador*" required>
        </div>
        <div class="row form-field">
            <div class="col-sm-4">
                <input name="Funcao" type="text" placeholder="Função*" required>
            </div>
            <div class="col-sm-4">
                <input name="Jornada" type="text" placeholder="Jornada" required>
            </div>
            <div class="col-sm-4">
                <input name="Inicio" type="text" placeholder="Início*" required>
            </div>
        </div>
        <button type="submit" class="btn btn-default" onclick="Processa_Dados()">Enviar</button>
    </form>
</div>

<script type="text/javascript">
    function Processa_Dados() {   
        var inscricao = document.getElementById("doutorado")
        var campoUm = inscricao.Orientador
        alert(campoUm.value)
    }
</script>
