import bibtexparser

with open('../publicacoes.bib') as bibtex_file:
    bib = bibtexparser.load(bibtex_file)

print(bib.entries)
