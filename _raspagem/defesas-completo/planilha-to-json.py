import pandas as pd
import numpy as np
import datetime
import unicodedata

def rcc(s):  # remove_control_characters
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

trabalhos = pd.read_excel('teses-dissertacoes.xls', converters={'Defesa': str})

Aluno      = np.array(trabalhos.Aluno)
Orientador = np.array(trabalhos.Orientador)
Nivel      = np.array(trabalhos.Nivel)
Titulo     = np.array(trabalhos.Titulo)
Defesa     = np.array(trabalhos.Defesa)

# normalizando nivel (M/D/DD)
Nivel[Nivel=='(M)'] = 'M'
Nivel[Nivel=='(D)'] = 'D'
Nivel[Nivel=='(DD)'] = 'DD'

# criando data string
defesa_data = [datetime.datetime.fromisoformat(d) for d in Defesa]
defesa = [d.strftime('%Y/%m/%d') for d in defesa_data]


# criando arquivos YAML

dissertacoes = open('dissertacoes.yml', 'w')
teses= open('teses.yml', 'w')

for i in range(Aluno.size):
  text = '-\n'
  text += f'  titulo: \"{rcc(Titulo[i])}\"\n'
  text += f'  titulo_en: \"\"\n'
  text += f'  aluno: \"{rcc(Aluno[i])}\"\n'
  text += f'  orientador: \"{rcc(Orientador[i])}\"\n'
  text += f'  data: \"{defesa[i]}\"\n'
  if Nivel[i] == 'M':
    dissertacoes.write(text)
    dissertacoes.write('  tipo: M\n')
  elif Nivel[i] == 'D' or Nivel[i] == 'DD':
    teses.write(text)
    teses.write(f'  tipo: {Nivel[i]}\n')

dissertacoes.close()
teses.close()
