from scholarly import scholarly

author = scholarly.search_author_id('V4ycRTQAAAAJ')

pubs = scholarly.fill(author)
pub = pubs['publications'][0]['bib']['title']

query = next(scholarly.search_pubs(pub))  # depois de algumas chamadas, o Google bloqueia...
bib = scholarly.bibtex(query)
print(bib)

#query = scholarly.search_pubs("A density-based algorithm for discovering clusters in large spatial databases with noise")
#pub = next(query)
#print(pub)
#print(scholarly.bibtex(pub))
