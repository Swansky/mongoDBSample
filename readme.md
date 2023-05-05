

# Objectif

##### Modélisation données d'une equipe de foot de la maniere suivante
###### Equipe:
- Nom
- Couleur
- Stade
- Effectif (liste des joueurs)

###### Modélisation joueur:
- nom
- prenom
- date de naissance
- taille poids
- poste

###### Modélisation match:
- equipe domicile
- equipe exterieur
- compétition
- score equipe domicile
- score equipe exterieur
- note des joueurs domicile 
- note des joueurs exterieur


##### format des collections en json



Equipe
```json
{
    "_id": ObjectId("..."),
    "nom": "Paris Saint-Germain",
    "couleur": "bleu et rouge",
    "stade": "Parc des Princes",
    "effectif": [
        ObjectId("..."), // ID du joueur 1
        ObjectId("..."), // ID du joueur 2
        ...
    ]
}

```

Joueurs:
```json
{
    "_id": ObjectId("..."),
    "nom": "Mbappé",
    "prenom": "Kylian",
    "date_naissance": ISODate("1998-12-20"),
    "taille": 178,
    "poids": 73,
    "poste": "attaquant"
}
```

matches:
```json
{
    "_id": ObjectId("..."),
    "equipe_domicile": ObjectId("..."), // ID de l'équipe domicile
    "equipe_exterieur": ObjectId("..."), // ID de l'équipe extérieur
    "competition": "Ligue 1",
    "score_equipe_domicile": 2,
    "score_equipe_exterieur": 1,
    "note_joueurs_domicile": [
        { "joueur": ObjectId("..."), "note": 8 },
        { "joueur": ObjectId("..."), "note": 7 },
        ...
    ],
    "note_joueurs_exterieur": [
        { "joueur": ObjectId("..."), "note": 6 },
        { "joueur": ObjectId("..."), "note": 5 },
        ...
    ]
}

```


#####  Optimisation des requetes sur certaines champs
Sur la collection joueur 

```js
// Sur le champs "nom" de la collection joueur
db.joueurs.ensureIndex({"nom":1});
// Sur le champs "nom" de la collection equipe
db.equipe.ensureIndex({"nom":1});
```


Selection des joueurs pour un poste et un age max
```js
db.joueurs.find({
"poste":"arriere droit",
"age" : {$lt :25}
})
```

```js
db.joueurs.aggregate([
    // Étape 1 : Faire une jointure entre les collections "joueurs" et "matches" via "effectif" dans la collection "equipes"
    {
        $lookup: {
            from: "equipes",
            localField: "_id",
            foreignField: "effectif",
            as: "equipes"
        }
    },
    
    // Étape 2 : Aplatir la collection "equipes" pour avoir une collection de documents de matches
    {
        $unwind: "$equipes"
    },
    
    // Étape 3 : Regrouper les documents de matches par joueur et compter le nombre de matches
    {
        $group: {
            _id: "$equipes.effectif",
            nb_matches: { $sum: 1 },
            note_totale: {
                $sum: {
                    $cond: [
                        { $eq: ["$equipes.effectif", "$note_joueurs_domicile.joueur"] },
                        "$note_joueurs_domicile.note",
                        {
                            $cond: [
                                { $eq: ["$equipes.effectif", "$note_joueurs_exterieur.joueur"] },
                                "$note_joueurs_exterieur.note",
                                0
                            ]
                        }
                    ]
                }
            }
        }
    },
    
    // Étape 4 : Filtrez les joueurs qui ont joué au moins 3 matchs
    {
        $match: {
            nb_matches: { $gte: 3 }
        }
    },
    
    // Étape 5 : Calculer la moyenne des notes par joueur
    {
        $project: {
            _id: 1,
            nb_matches: 1,
            moyenne_notes: { $divide: [ "$note_totale", "$nb_matches" ] }
        }
    },
    
    // Étape 6 : Enregistrer les résultats dans une nouvelle collection
    {
        $out: "joueurs_notes_moyennes"
    }
]);
```


structure de la nouvelle collection
```js
{
    "_id": ObjectId("..."), // id joueur
    "nb_matches": 3,
    "moyenne_notes": 7.5
}
```



