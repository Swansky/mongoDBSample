from pymongo import MongoClient
from dateutil import parser

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb://root:example@localhost:27017"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)

# Create the database for our example (we will use the same database throughout the tutorial
database = client['database']

playersCollection = database['players']
equipeCollection = database['equipes']
matchesCollection = database['matches']

player1 = {
    "nom": "Mbappé",
    "prenom": "Kylian",
    "date_naissance": parser.parse("1998-12-20"),
    "taille": 178,
    "poids": 73,
    "poste": "attaquant"
}

player2 = {
    "nom": "Neymar",
    "prenom": "Jr",
    "date_naissance": parser.parse("1992-02-05"),
    "taille": 175,
    "poids": 68,
    "poste": "attaquant"
}

player1ID = playersCollection.insert_one(player1).inserted_id
player2ID = playersCollection.insert_one(player2).inserted_id

equipe1 = {
    "nom": "Paris Saint-Germain",
    "couleur": "bleu et rouge",
    "stade": "Parc des Princes",
    "effectif": [
        player1ID
    ]
}

equipe2 = {
    "nom": "FC Barcelone",
    "couleur": "bleu et rouge",
    "stade": "Camp Nou",
    "effectif": [
        player2ID
    ]
}

equipe1ID = equipeCollection.insert_one(equipe1).inserted_id
equipe2ID = equipeCollection.insert_one(equipe2).inserted_id

match1 = {
    "equipe_domicile": equipe1ID,
    "equipe_exterieur": equipe2ID,
    "competition": "Ligue des Champions",
    "score_equipe_domicile": 2,
    "score_equipe_exterieur": 1,
    "note_joueurs_domicile": [
        {"joueur": player1ID, "note": 8},

    ],
    "note_joueurs_exterieur": [
        {"joueur": player2ID, "note": 6}
    ]
}

matchesCollection.insert_one(match1)
