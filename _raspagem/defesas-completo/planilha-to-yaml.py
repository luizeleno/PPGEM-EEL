import pandas as pd
import numpy as np
import datetime
import unicodedata

def rcc(s):  # remove_control_characters
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

trabalhos = pd.read_excel('teses-dissertacoes.xls', converters={'Data': str})

Aluno      = np.array(trabalhos.Aluno)
Orientador = np.array(trabalhos.Orientador)
Banca      = np.array(trabalhos.Banca)
Nivel      = np.array(trabalhos.Nivel)
Titulo     = np.array(trabalhos.Titulo)
Data     = np.array(trabalhos.Data)

# normalizando nivel (M/D/DD)
Nivel[Nivel=='(M)'] = 'M'
Nivel[Nivel=='(D)'] = 'D'
Nivel[Nivel=='(DD)'] = 'DD'

# verificando horarios não fornecidos
Horario  = trabalhos.Horario
nohorarios = Horario.isnull()
Horario  = np.array(Horario)
nohorarios = np.array(nohorarios)

# criando data string
defesa_data = [datetime.datetime.fromisoformat(d) for d in Data]
defesa = [d.strftime('%Y/%m/%d') for d in defesa_data]

# verificando titulos em inglês ausentes
Title = trabalhos.Title
notitle = Title.isnull()
Title     = np.array(Title)
nottitle = np.array(notitle)

# criando arquivos YAML

dissertacoes = open('../../_data/dissertacoes.yml', 'w')
teses= open('../../_data/teses.yml', 'w')

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
  if Nivel[i] == 'M':
    dissertacoes.write(text)
    dissertacoes.write('  tipo: M\n')
  elif Nivel[i] == 'D' or Nivel[i] == 'DD':
    teses.write(text)
    teses.write(f'  tipo: {Nivel[i]}\n')

dissertacoes.close()
teses.close()
