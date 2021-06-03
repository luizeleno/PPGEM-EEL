import json
import bibtexparser
import pandas
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

with open('../publicacoes.bib') as bibtex_file:
    bib = bibtexparser.load(bibtex_file);

with open('publicacoes-citacoes.json') as json_file:
    cites = json.load(json_file);

chrono = {}

for publi in bib.entries:
    y = int(publi['year'])
    doi = publi['doi']
    try:
        cit = cites[doi]
    except:
        cit = 0

    if y in chrono:
        chrono[y]['publications'] += 1
        chrono[y]['citations'] += cit
    else:
        chrono[y] = {'publications': 1, 'citations': cit}

data = pandas.DataFrame.from_dict(chrono, orient='index')
data.sort_index(inplace=True)
datasum = data.cumsum()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.set_xlabel('Ano')
ax1.set_ylabel('Publicações', color='b')
ax2.set_ylabel('Citações', color='r')

ax1.plot(datasum['publications'], 'b')
ax2.plot(datasum['citations'], 'r')

plt.tight_layout()
plt.show()
