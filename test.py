# Librairies
from datetime import datetime, date



# Ajouter un fichier de type text dans le répertoire outputs à chaque exécution de scripts
now = datetime.now()
day = date.today()

with open(f'outputs/Log_{day}.txt', 'w') as fichier:
    fichier.write(f'{now}')