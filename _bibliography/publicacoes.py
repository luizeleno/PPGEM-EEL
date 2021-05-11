import os
import json
from habanero import cn

# diretório com doi files por pocente
docentes_dir = './docentes/'

# criando dicionário docentes = {docente: [doi_list]}
docentes = {}
walk = os.walk('./docentes/')
doi_files = list(walk)[0][-1]
for docente_doi in doi_files:
    with open(docentes_dir + docente_doi, 'r') as doi_file:
        doi_list = doi_file.readlines()
    doi_list = [s.strip('\n') for s in doi_list]
    docente = docente_doi.split('.')[0]
    docentes[docente] = doi_list

with open('docentes.json', 'w') as doc:
    json.dump(docentes, doc)

#criando conjunto de doi completo
doi_set = set()
for doc, doi in docentes.items():
    doi_set |= set(doi)
with open('publicacoes.doi', 'w') as doc:
    for doi in doi_set:
        doc.write(doi + '\n')
    
#criando dicionario publicacoes = {doi: bibentry}
publicacoes = {}
for doi in doi_set:
    try:
        entry = cn.content_negotiation(ids=pub)
        publicacoes[doi] = entry
    except:
        print(f'AVISO: não consegui encontrar {doi}')
with open('publicacoes.json', 'w') as doc:
    json.dump(list(publicacoes), doc)


#criando bibfile geral

#criando bibfile  por docente

#------------------

#for docente_doi in doi_files:
    
    #docente = docente_doi.split('.')[0]
    #print(docente)
    
    #try:
        #with open(included_doi_dir + docente_doi, 'r') as doi_file:
            #doi_list = doi_file.readlines()
        #doi_list = set([s.strip('\n') for s in doi_list])
    #except:
        #doi_list = set()
        #with open(included_doi_dir + docente_doi, 'w') as doi_file:
            #doi_file.write('')
    
    #new_doi = set()
    #with open(doi_dir + docente_doi, 'r') as doc:
        #doc_doi = doc.readlines()
    #doc_doi = [s.strip('\n') for s in doc_doi]
    #new_doi |= set(doc_doi)
    
    #new_doi = set([x for x in new_doi if x not in doi_list])  # new doi list
    #doi_list |= new_doi  # updated doi list
    
    #buscando dados de novas referências
    #n, i = len(new_doi), 1
    #print(f' Consultando {n} referências...')
    #with open(included_bib_dir + f'{docente}.bib', 'a') as bib:
        #for doi in new_doi:
            #try:
                #print(f'{i}/{n}: {doi}')
                #ref = cn.content_negotiation(ids=doi)
                #bib.write(ref+'\n\n')
            #except:
                #print(f'AVISO: não consegui encontrar {doi}')
            #i += 1
    
    #reescrevendo lista de referência já lidas
    #doi_set = set(doi_list)
    #with open(included_doi_dir + docente_doi, 'w') as doi_file:
        #for doi in doi_set:
            #doi_file.write(doi + '\n')

#Criando lista completa de referências
#bib_files = [included_bib_dir + x.split('.')[0] + '.bib' for x in doi_files]
#bib_files = ' '.join(bib_files)
#os.system(f'bibtool -f "%n(author):%4d(year)" {bib_files} -o publicacoes.bib');
