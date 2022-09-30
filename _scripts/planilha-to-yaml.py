import pandas as pd
import numpy as np
import datetime
import unicodedata

def rcc(s):  # remove_control_characters
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

# criando arquivos YAML
dissertacoes = open('../_data/dissertacoes.yml', 'w')
teses= open('../_data/teses.yml', 'w')

for n, nivel in zip(range(3), ('D', 'DD', 'M')):

    trabalhos = pd.read_csv('defesas.csv.'+f'{n}', converters={'Data': str})

    Aluno      = np.array(trabalhos.Aluno)
    Orientador = np.array(trabalhos.Orientador)
    Banca      = np.array(trabalhos.Banca)
    Titulo     = np.array(trabalhos.Titulo)
    Data       = np.array(trabalhos.Data)

    # verificando horarios não fornecidos
    Horario  = trabalhos.Horario
    nohorarios = Horario.isnull()
    Horario  = np.array(Horario)
    nohorarios = np.array(nohorarios)

    # criando data string
    defesa_data = [datetime.datetime.fromisoformat(d.replace('/', '-')) for d in Data]
    defesa = [d.strftime('%Y/%m/%d') for d in defesa_data]

    # verificando titulos em inglês ausentes
    Title = trabalhos.Title
    notitle = Title.isnull()
    Title     = np.array(Title)
    nottitle = np.array(notitle)

    for i in range(Aluno.size):
        text = '-\n'
        text += f'  titulo: \"{rcc(Titulo[i])}\"\n'
        text += f'  aluno: \"{rcc(Aluno[i])}\"\n'
        text += f'  orientador: \"{rcc(Orientador[i])}\"\n'
        text += f'  banca: \"{rcc(Banca[i])}\"\n'
        text += f'  data: \"{defesa[i]}\"\n'

        if not nohorarios[i]:
            text += f'  horario: \"{rcc(Horario[i])}\"\n'
        if not notitle[i]:
            text += f'  titulo_en: \"{rcc(Title[i])}\"\n'

        # escrevendo arquivos YAML
        if n >= 2:
            dissertacoes.write(text)
            dissertacoes.write('  tipo: M\n')
        else:
            teses.write(text)
            teses.write(f'  tipo: {nivel}\n')

dissertacoes.close()
teses.close()
