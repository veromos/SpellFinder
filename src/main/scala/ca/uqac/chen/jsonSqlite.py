import sqlite3
import json
from datetime import datetime

#Connexion à la base de données
connexion = sqlite3.connect("C:\sqlite\exercice1.db")

#Charger le fichier JSON
with open('C:\sqlite\spells2.json', encoding='utf-8-sig') as json_file:
    #Lecture de fichier
    json_data = json.loads(json_file.read())

#Recupere la liste de colonnes.
    columns = []
    data = json_data.get('spell')
    for col in data:
            if col not in columns:
                columns.append(col)

#Création d’un curseur sur la base:
curseur = connexion.cursor()

# creation des tables
curseur.execute("DROP TABLE tableSpell")
curseur.execute("CREATE TABLE IF NOT EXISTS tableSpell(id TEXT, name TEXT, levels TEXT, components TEXT, spell_resistance TEXT)")

print("insert has started at " + str(datetime.now()))
for c in columns:
    val_id = c.get('id')
    val_name = c.get('name')
    val_levels = c.get('levels')
    val_components = c.get('components')
    val_spell_resistance = c.get('spell_resistance')
    curseur.execute("insert into tableSpell values (?,?,?,?,?)",(val_id,val_name,str(val_levels),str(val_components), val_spell_resistance))

connexion.commit()
curseur.close()
print("insert has completed at " + str(datetime.now()))