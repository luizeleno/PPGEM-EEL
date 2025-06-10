#! /usr/bin/bash

echo '############################################################' 
echo `date`

echo '############################################################' 
echo "# Sincronizando com o Google Drive..."
cd /home/eleno/Dropbox/Lorena/Website/PPGEM-EEL/_Drive
rclone sync GoogleDrive:PPGEM-site .

echo '############################################################' 
echo '# Atualizando publicações...'
cd ../_bibliography
source .venv/bin/activate
python3 publicacoes.py

echo '############################################################' 
echo '# Atualizando defesas...'
cd ../_scripts
ssconvert -S  ../_Drive/Defesas/DEFESAS-PPGEM-EEL.xlsx defesas.csv
python3 planilha-to-yaml.py

echo '############################################################'
echo "# Atualizando o site no Github..."
cd ..
rake build
rake commit

echo '############################################################' 
echo "Done!"
