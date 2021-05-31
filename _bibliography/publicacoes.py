import os
import json
import pandas
import habanero

# diretório com arquivos xlsx com os DOI
docentes_dir = '../_Drive/Publicacoes/'

# criando dicionário docentes = {docente: [doi_list]}
docentes = {}
walk = os.walk(docentes_dir)
xslx_files = list(walk)[0][-1]
for docente_xlsx in xslx_files:
    data = pandas.read_excel(docentes_dir + docente_xlsx)
    doi_list = data['DOI']
    doi_list = set([s.strip('\n') for s in doi_list])
    docente = docente_xlsx.split('.')[0]
    docentes[docente] = list(doi_list)
with open('docentes.json', 'w') as doc:
    json.dump(docentes, doc)

# lista de doi já lidos
try:
    with open('publicacoes.doi', 'r') as doi_file:
        doi_lidos = doi_file.readlines()
    doi_lidos = [s.strip('\n') for s in doi_lidos]
except:
    os.system('touch publicacoes.doi')
    doi_lidos = set()
try:
    with open('publicacoes.json', 'r') as doc:
        publicacoes = json.load(doc)
except:
    publicacoes = {}

# criando conjunto de doi completo
doi_set = set()
for doc, doi in docentes.items():
    doi_set |= set(doi)
with open('publicacoes.doi', 'w') as doc:
    for doi in doi_set:
        doc.write(doi + '\n')
    
# criando dicionario publicacoes = {doi: bibentry}
n, i = len(doi_set), 1
for doi in doi_set:
    if doi not in doi_lidos:
        try:
            print(f'{i}/{n}: {doi}')
            entry = habanero.cn.content_negotiation(ids=doi)
            publicacoes[doi] = entry
        except:
            print(f'{i}/{n} {doi}: AVISO: não consegui encontrar {doi}')
    else:
        print(f'{i}/{n}: AVISO: {doi} já na base')
    i += 1
with open('publicacoes.json', 'w') as doc:
    json.dump(publicacoes, doc)

# criando bibfile geral
with open('publicacoes.bib', 'w') as bib:
    for doi, entry in publicacoes.items():
        try:
            bib.write(entry + '\n\n')
        except:
            pass
os.system(f'bibtool -f "%n(author):%4d(year)" publicacoes.bib -o publicacoes.bib');

# criando bibfiles por docente
for docente, doi_list in docentes.items():
    with open(f'{docente}.bib', 'w') as doc:
        for doi in doi_list:
            try:
                doc.write(publicacoes[doi]+'\n')
            except:
                print(f'AVISO: problema no doi {doi} do docente {docente}')
    os.system(f'bibtool -f "%n(author):%4d(year)" {docente}.bib -o {docente}.bib');
