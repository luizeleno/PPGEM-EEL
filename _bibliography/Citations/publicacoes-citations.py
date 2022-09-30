import habanero
import json

with open ('../publicacoes.doi') as doi_file:
    doi_list = doi_file.readlines()
doi_list = set([doi.strip('\n') for doi in doi_list])

doi_dict = {}
n, i = len(doi_list), 1
for doi in doi_list:
    try:
        print(f'{i}/{n}: {doi} ')
        citations = habanero.counts.citation_count(doi=doi)
        doi_dict[doi] = citations
    except:
        print(f'{i}/{n}: AVISO - erro em {doi} ')
    i += 1

with open('publicacoes-citacoes.json', 'w') as doc:
    json.dump(doi_dict, doc)
