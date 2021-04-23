#! /usr/bin/bash

cd /home/eleno/Dropbox/Lorena/Website/PPGEM-EEL/_Drive

# sincronizando com o Google Drive
rclone sync edrf:PPGEM-site .

cd ..

# atualizando o site no Github
rake build
rake commit

# voltando ao home
cd
