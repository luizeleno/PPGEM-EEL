import pandas
import os

doi_dir = './doilist/'

doi_set = set()
for root, dirs, files in os.walk(doi_dir):
    for docente in files:
        print(docente)
        with open(doi_dir + docente, 'r') as doc:
            doi_list = doc.readlines()
        doi_list = [s.strip('\n') for s in doi_list]
        doi_set |= set(doi_list)

os.system('touch publicacoes.bib')
os.system('truncate -s 0 publicacoes.bib')

n, i = len(doi_set), 1
for doi in doi_set:
    print(f'{i}/{n}: {doi}')
    os.system(f'doi2bib "{doi}" >> publicacoes.bib')
    i += 1
