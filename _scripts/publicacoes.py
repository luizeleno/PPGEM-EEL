import pandas
import os

pubs = pandas.read_excel('/home/eleno/Dropbox/Lorena/Website/PPGEM-EEL/_Drive/Publicacoes/Publicacoes.xlsx')

os.system('touch publicacoes.bib')
os.system('truncate -s 0 publicacoes.bib')

for doi in pubs['DOI']:
    print(doi)
    os.system(f'doi2bib {doi} >> publicacoes.bib')
