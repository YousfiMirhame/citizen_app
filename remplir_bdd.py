import sqlite3

# Connexion (ou création) de la base de données
conn = sqlite3.connect('citizens.db')
cursor = conn.cursor()

# Création de la table s'il n'existe pas déjà
cursor.execute('''
CREATE TABLE IF NOT EXISTS citoyens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code_barre TEXT,
    nom TEXT,
    prenom TEXT,
    adresse TEXT,
    date_naissance TEXT,
    photo TEXT
)
''')

# Insertion des citoyens
citoyens = [
    ("123456789", "Aidouni", "Sofiane", "12 rue de Offenburg", "1991-01-31", "sofiane.jpg"),
    ("876543219", "Yousfi", "Mirhame", "34 avenue de Stuttgart", "1994-06-23", "mirhame.jpg"),
    ("987654691", "Martin", "Claire", "04 avenue de Berlin", "1982-05-13", "claire.jpg")
]

cursor.executemany('''
    INSERT INTO citoyens (code_barre, nom, prenom, adresse, date_naissance, photo)
    VALUES (?, ?, ?, ?, ?, ?)
''', citoyens)

conn.commit()
conn.close()

print("✅ Base de données remplie avec succès.")
