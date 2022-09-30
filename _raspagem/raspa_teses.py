from bs4 import BeautifulSoup
import unicodedata

def rcc(s):  # remove_control_characters
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")

def parse_data(data):  # transforma dd/mm/aaaa para aaaa/mm/dd
    dma = data.split('/')
    dma = list(map(int, dma))
    return f'{dma[2]:04d}/{dma[1]:02d}/{dma[0]:02d}'


def raspa(doc, tipo='Tese de Doutorado', arq='teses.yml'):

    with open(doc, 'r') as html:
        soup = BeautifulSoup(html, 'html.parser')

    tds = soup.find_all('td')

    with open(arq, 'w') as f:

        for td in tds:
            class_ = td.get('class', [])
            style_ = td.get('style', [])
            width_ = td.get('width', [])

            if class_ == ['art-postmetadatafooter'] and style_ == 'text-align:justify;':
                print(f'- \n  titulo: "{rcc(td.text)}"', file=f)
            elif class_ == ['bordacelula']:
                if width_ == '85%':
                    print(f'  aluno: "{rcc(td.text)}"', file=f)
                else:   
                    data = td.findChildren('span')
                    if data:
                        dma = parse_data(data[0].text)
                        print(f'  data: "{rcc(dma)}"', file=f)
                    else :
                        print(f'  orientador: "{(rcc(td.text).strip())}"', file=f)
                        print(f'  tipo: "{rcc(tipo)}"', file=f)


teses = 'teses-defendidas.html'
dissertacoes = 'dissertacoes-defendidas.html'

raspa(teses)
raspa(dissertacoes, tipo="Dissertação de Mestrado", arq='dissertacoes.yml')
