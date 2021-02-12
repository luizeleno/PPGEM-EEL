from bs4 import BeautifulSoup
with open("teses-defendidas.html", "r") as html:
    soup = BeautifulSoup(html, 'html.parser')

titles = soup.findAll("td", {"class": "art-postmetadatafooter", "style": "text-align:justify;"})

alunos = soup.findAll("td", {"class": "bordacelula", "width": "85%"})

#### ainda não funciona:
orientador = soup.findAll("td", {"class": "bordacelula", "width": ""})
[print(a.text) for a in orientador]

data = soup.findAll("span", {"class": "date-display-single"})
# [print(a.text) for a in data]