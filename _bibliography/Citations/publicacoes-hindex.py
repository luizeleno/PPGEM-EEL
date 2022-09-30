import pandas
import json

with open('publicacoes-citacoes.json') as json_file:
    data = json.load(json_file);

z = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}

print(z)
