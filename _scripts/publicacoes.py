import pandas
import os

pubs = pandas.read_excel('Publicacoes.xlsx')

os.system('touch publicacoes.bib')
os.system('truncate -s 0 publicacoes.bib')

doilist = set(pubs['DOI'])  # elimina repetidas
n = len(doilist)

i = 1
for doi in doilist:
    print(f'{i}/{n}: {doi}')
    os.system(f'doi2bib "{doi}" >> publicacoes.bib')
    i += 1
