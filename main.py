from pymongo import MongoClient
from dateutil import parser
from random import randint

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb://root:example@localhost:27017"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)

# Create the database for our example (we will use the same database throughout the tutorial
database = client['database']

#Ajout des collections
playersCollection = database['players']
equipeCollection = database['equipes']
matchesCollection = database['matches']

def create_player(nom, prenom, date_naissance, taille, poids, poste):
    player = {
        "nom": nom,
        "prenom": prenom,
        "date_naissance": parser.parse(date_naissance),
        "taille": taille,
        "poids": poids,
        "poste": poste
    }
    playersCollection.insert_one(player)
    return player

def create_team(nom, couleur, stade, effectif):
    equipe = {
        "nom": nom,
        "couleur": couleur,
        "stade": stade,
        "effectif": effectif
    }
    equipeCollection.insert_one(equipe)
    return equipe

def create_note_joueur(joueur, note):
    note_joueur = {
        "joueur": joueur,
        "note": note
    }
    return note_joueur

def create_match(equipe_domicile, equipe_exterieur, competition, score_equipe_domicile, score_equipe_exterieur, note_joueurs_domicile, note_joueurs_exterieur):
    match = {
        "equipe_domicile": equipe_domicile,
        "equipe_exterieur": equipe_exterieur,
        "competition": competition,
        "score_equipe_domicile": score_equipe_domicile,
        "score_equipe_exterieur": score_equipe_exterieur,
        "note_joueurs_domicile": note_joueurs_domicile,
        "note_joueurs_exterieur": note_joueurs_exterieur
    }
    matchesCollection.insert_one(match)
    return match



#Ajout des joueurs
player1 = create_player("Mark", "Evans", "1998-12-20", 178, 73, "Gardien")
player2 = create_player("Nathan", "Swift", "1992-02-05", 175, 68, "Défenseur")
player3 = create_player("Jack", "Wallse", "1997-03-05", 200, 150, "Défenseur")
player4 = create_player("Bobby", "Shearer", "1995-04-06", 180, 55, "Défenseur")
player5 = create_player("Tod", "IronSe", "1996-03-04", 120, 34, "Défenseur")
player6 = create_player("Erik", "Eagle", "1991-02-05", 165, 54, "Milieu")
player7 = create_player("Timmy", "Saunders", "1993-05-07", 175, 63, "Milieu")
player8 = create_player("Jude", "Sharp", "1993-05-07", 175, 62, "Milieu")
player9 = create_player("Maxwell", "Carson", "1995-06-08", 175, 63, "Milieu")
player10 = create_player("Axel", "Blaze", "1996-05-07", 180, 60, "Attaquant")
player11 = create_player("Kevin", "Dragonfly", "1990-11-11", 171, 69, "Attaquant")
player12 = create_player("William Willy", "Glass", "1997-05-07", 156, 47, "Attaquant")
player13 = create_player("Jim", "Wraith", "1992-04-09", 189, 61, "Défenseur")
player14 = create_player("Sam", "Kinca", "1993-07-07", 165, 51, "Milieu")
player15 = create_player("Steve", "Grim", "1994-10-07", 170, 60, "Milieu")
Poseidon = create_player("Paul", "Sdon", "1995-10-07", randint(130,200), randint(35,75), "Gardien")
Apollon = create_player("Apollo", "Light", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
Hephaistos = create_player("Jeff", "Iron", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
Ares = create_player("Lane", "War", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
Dionysos = create_player("Danny", "Wood", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
Artemis = create_player("Artie", "Mishman", "1995-10-07", randint(130,200), randint(35,75), "Milieu")
Hermes = create_player("Arion", "Matlock", "1995-10-07", randint(130,200), randint(35,75), "Milieu")
Athena = create_player("Wesley", "Knox", "1995-10-07", randint(130,200), randint(35,75), "Milieu")
Demeter = create_player("Jonas", "Demetrius", "1995-10-07", randint(130,200), randint(35,75), "Attaquant")
Aphrodite = create_player("Byron", "Love", "1995-10-07", 171, 45, "Milieu")
Hera = create_player("Henry", "House", "1995-10-07", randint(130,200), randint(35,75), "Attaquant")
Icare = create_player("Iggy", "Russ", "1995-10-07", randint(130,200), randint(35,75), "Gardien")
Achille = create_player("Gus", "Heeley", "1995-10-07", randint(130,200), randint(35,75), "Attaquant")
Heracles = create_player("Harry", "Closs", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
Chronos = create_player("Andy", "Chronic", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
Meduse = create_player("Ned", "Yousef", "1995-10-07", randint(130,200), randint(35,75), "Milieu")

player16 = create_player("Shawn", "Frost", "1995-10-07", randint(130,200), randint(35,75), "Gardien")
player17 = create_player("Axel", "Blaze", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
player18 = create_player("Jude", "Sharp", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
player19 = create_player("Nathan", "Swift", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
player20 = create_player("Kevin", "Dragonfly", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
player21 = create_player("Jim", "Wraith", "1995-10-07", randint(130,200), randint(35,75), "Milieu")
player22 = create_player("Steve", "Grim", "1995-10-07", randint(130,200), randint(35,75), "Milieu")
player23 = create_player("Sam", "Kinca", "1995-10-07", randint(130,200), randint(35,75), "Milieu")
player24 = create_player("Mark", "Evans", "1995-10-07", randint(130,200), randint(35,75), "Attaquant")
player25 = create_player("Bobby", "Shearer", "1995-10-07", randint(130,200), randint(35,75), "Milieu")
player26 = create_player("Tod", "IronSe", "1995-10-07", randint(130,200), randint(35,75), "Attaquant")
player27 = create_player("Maxwell", "Carson", "1995-10-07", randint(130,200), randint(35,75), "Gardien")
player28 = create_player("Erik", "Eagle", "1995-10-07", randint(130,200), randint(35,75), "Attaquant")
player29 = create_player("William Willy", "Glass", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")
player30 = create_player("Timmy", "Saunders", "1995-10-07", randint(130,200), randint(35,75), "Défenseur")



effectif_equipe1 = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11,player12]
effectif_equipe2 = [Poseidon, Apollon, Hephaistos, Ares, Dionysos, Artemis, Hermes, Athena, Demeter, Aphrodite, Hera, Icare]
effectif_equipe3 = [player16, player17, player18, player19, player20, player21, player22, player23, player24, player25, player26,player27]
#Créations des équipes


team1 = create_team("Raimon", "Jaune et bleu", "Stade Raimon",effectif_equipe1)
team2 = create_team("Zeus", "Vert, Jaune et Blanc", "Zeus Stadium", effectif_equipe2)
team3 = create_team("Royal Académie", "Vert et Rouge", "Stade Impérial", effectif_equipe3)

#Création des notes des joueurs
note_random_team1 = []
note_random_team2 = []
note_random_team3 = []

for i in range(0, len(effectif_equipe1)):
    note_random_team1.append(create_note_joueur(effectif_equipe1[i], randint(1,10)))
    note_random_team3.append(create_note_joueur(effectif_equipe3[i], randint(1,10)))
    note_random_team2.append(create_note_joueur(effectif_equipe2[i], randint(1,10)))


match1 = create_match(team1, team2, "Coupe du monde", 2, 1, note_random_team1, note_random_team2)
match2 = create_match(team1, team3, "Coupe du monde", 3, 1, note_random_team1, note_random_team3)
match3 = create_match(team2, team3, "Coupe du monde", 2, 2, note_random_team2, note_random_team3)    





