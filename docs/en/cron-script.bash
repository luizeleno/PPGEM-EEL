#! /usr/bin/bash

echo '#' `date`

echo "Sincronizando com o Google Drive..."
cd /home/eleno/Dropbox/Lorena/Website/PPGEM-EEL/_Drive
rclone sync edrf:PPGEM-site .

echo 'Atualizando defesas'
cd ../_scripts
python3 planilha-to-yaml.py

echo "# Atualizando o site no Github..."
cd ..
rake build
rake commit

echo "Done!"
