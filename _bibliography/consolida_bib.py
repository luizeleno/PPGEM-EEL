import os

bib_dir = './bib/'
files = list(os.walk(bib_dir))
bib = files[0][-1]

# autogerar bibkeys
[os.system(f'bibtool -k {bib_dir}/{x}') for x in bib]

#s = ''
#for x in bib: s += x + ' '
#os.system(f'bibtool')
