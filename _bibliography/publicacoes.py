import pandas
import os

# lista de referências já incluídas
try:
    with open('publicacoes.doi', 'r') as doi_file:
        doi_list = doi_file.readlines()
    doi_list = set([s.strip('\n') for s in doi_list])
except:
    doi_list = set()
    with open('publicacoes.doi', 'w') as doi_file:
        doi_file.write('')

# obtendo novas publicacoes
doi_dir = './doilist/'
new_doi = set()
for root, dirs, files in os.walk(doi_dir):
    for docente in files:
        print(docente)
        with open(doi_dir + docente, 'r') as doc:
            doc_doi = doc.readlines()
        doc_doi = [s.strip('\n') for s in doc_doi]
        new_doi |= set(doc_doi)

new_doi = set([x for x in new_doi if x not in doi_list])  # new doi list
doi_list |= new_doi  # updated doi list

# buscando dados de novas referências
n, i = len(new_doi), 1
for doi in new_doi:
    print(f'{i}/{n}: {doi}')
    os.system(f'doi2bib "{doi}" >> publicacoes.bib')
    i += 1

# reescrevendo lista de referência já lidas
doi_set = set(doi_list)
with open('publicacoes.doi', 'w') as doi_file:
    for doi in doi_set:
        doi_file.write(doi + '\n')
