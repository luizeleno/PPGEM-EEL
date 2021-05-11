import os
from habanero import cn

# obtendo novas publicacoes
doi_dir = './docentes_doi/'
for root, dirs, files in os.walk(doi_dir):
    for docente_doi in files:
        
        docente = docente_doi.split('.')[0]
        print(docente)
        
        # lista de referências já incluídas
        included_doi_dir = './doi/'
        included_bib_dir = './bib/'
        try:
            os.mkdir(included_doi_dir)
            os.mkdir(included_bib_dir)
        except FileExistsError:
            pass
        
        try:
            with open(included_doi_dir + docente_doi, 'r') as doi_file:
                doi_list = doi_file.readlines()
            doi_list = set([s.strip('\n') for s in doi_list])
        except:
            doi_list = set()
            with open(included_doi_dir + docente_doi, 'w') as doi_file:
                doi_file.write('')
        
        new_doi = set()
        with open(doi_dir + docente_doi, 'r') as doc:
            doc_doi = doc.readlines()
        doc_doi = [s.strip('\n') for s in doc_doi]
        new_doi |= set(doc_doi)

        new_doi = set([x for x in new_doi if x not in doi_list])  # new doi list
        doi_list |= new_doi  # updated doi list

        # buscando dados de novas referências
        n, i = len(new_doi), 1
        print(f' Consultando {n} referências...')
        with open(included_bib_dir + f'{docente}.bib', 'w') as bib:
            for doi in new_doi:
                try:
                    print(f'{i}/{n}: {doi}')
                    ref = cn.content_negotiation(ids=doi)
                    bib.write(ref+'\n\n')
                except:
                    print(f'AVISO: não consegui encontrar {doi}')
                i += 1

        # reescrevendo lista de referência já lidas
        doi_set = set(doi_list)
        with open(included_doi_dir + docente_doi, 'w') as doi_file:
            for doi in doi_set:
                doi_file.write(doi + '\n')
