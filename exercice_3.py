promotion = [
  {
  "nom" : "TOTO",
  "prenom":"Marcel",
  "notation" :
    [

      {
    "Sciences": {
    "notes" : [8,14,17,19],
    "observations":"Peut mieux faire"
        }
      },
      {
    "Maths": {
    "notes" : [12,14,17,19],
    "observations":"Très bien"
        }
      },
      
   ]
  },
  {
  "nom" : "DUBOIS",
  "prenom":"Jean-Michel",
  "notation" :
    [
      {
    "Sciences": {
    "notes" : [2,14,11,19],
    "observations":"Pas mal"
        }
      },
      {
    "Maths": {
    "notes" : [12,14,8,19],
    "observations":"Médiocre"
        }
      }
   ]
  },
    {
  "nom" : "COSATTINI",
  "prenom":"Thibault",
  "notation" :
    [
      {
    "Sciences": {
    "notes" : [20,14,11,19,20],
    "observations":"Pas mal"
        }
      },
      {
    "Maths": {
    "notes" : [12,14,8,19],
    "observations":"Médiocre"
        }
      }
   ]
  }
]


# 2.
def moyenneEtudiant(promotion,etudiantName) :
  specifiedEtudiantNotes = []
  for i in promotion :
    if i["nom"] == etudiantName :
      notations = i["notation"]
      for y in notations :
         notes = y[next(iter(y))]["notes"]
         for x in notes :
          specifiedEtudiantNotes.append(x)

  return "La moyenne générale de", etudiantName ,"=", sum(specifiedEtudiantNotes)/len(specifiedEtudiantNotes)

# print(moyenneEtudiant(promotion,"TOTO"))


# 3.
def moyennePromotionMatiere(promotion, matiere) :
  specifiedNotes = []
  for i in promotion :
      notations = i["notation"]
      for y in notations :
        if next(iter(y)) == matiere :
          notes = y[matiere]
          for x in notes["notes"] :
                specifiedNotes.append(x)

  return "La moyenne de la promotion pour la matière" +  matiere + "=" + str(sum(specifiedNotes)/len(specifiedNotes))

# print(moyennePromotionMatiere(promotion,"Sciences"))


# 4 & 5
def moyenneMaxEtudiant(promotion) :
  specifiedMoyenne = []
  moyennes = []
  for i in promotion  :
      etudiantArray = []
      notations = i["notation"]
      specifiedMoyenne.append(etudiantArray)
      for y in notations :
        moyenneEtudiant = []
        notes = y[next(iter(y))]["notes"]
        etudiantArray.append({"nom":i["nom"],"moyenne" :  sum(notes)/len(notes)})
      for x in etudiantArray :
        moyenneEtudiant.append((x["moyenne"]))
      etudiantArray.append({ "nom":i["nom"],"prenom":i["prenom"],"moyenne_gene": sum(moyenneEtudiant)/len(moyenneEtudiant)})
  for moyenne in specifiedMoyenne :
    moyennes.append(moyenne[-1])
  moyenneMax = max(moyennes, key=lambda x: x['moyenne_gene'])

  return "L'éleve ayant la meilleure moyenne générale est " + moyenneMax["prenom"] + " "+moyenneMax["nom"] +" "+ "avec" +" "+ str( moyenneMax["moyenne_gene"])

print(moyenneMaxEtudiant(promotion))



# Bonus
def moyenneEtudiantMatiere(promotion,etudiantName, matiere) :
  specifiedEtudiantNotes = []
  for i in promotion :
    if i["nom"] == etudiantName :
      notations = i["notation"]
      for y in notations :
        if next(iter(y)) == matiere :
          notes = y[matiere]
          for x in notes["notes"] :
                specifiedEtudiantNotes.append(x)
  return "La moyenne de" +" "+etudiantName + " "+ "pour la matière"+ " "+ matiere + " "+ "=" + " "+str(sum(specifiedEtudiantNotes)/len(specifiedEtudiantNotes))

# print(moyenneEtudiantMatiere(promotion,"TOTO","Sciences"))

