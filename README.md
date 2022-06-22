# SAE-24
Partie Web et BdD : Prérequis : 
- Le brocker envoie des données avec un ID unique, un timestamp, une pièce (par ex. Maison1) et une donnée : température. 
- Plusieurs capteurs (avec des ID différents) publieront des données. 
- La collecte de données se fera sous un système Linux Ubuntu dans une VM ou machine physique.
- Les données peuvent être enregistrées dans un fichier dans un format que vous définirez.

Schéma général : 
![image](https://user-images.githubusercontent.com/94040740/174994617-4c005822-9c63-47c6-855f-de70fabb9f0f.png)

Partie base de données :
- Sous Windows : VM ou natif
- Deux tables avec :
    ID, nom du capteur, pièce, emplacement du capteur : 
    l’ID est unique et ne peut pas être changé
    La pièce provient des informations du capteur
    Le nom et l’emplacement pourront être modifié dans la partie présentation des données
    A noter que le nom devra être unique comme l’ID
- Les données avec un timestamp et une clé étrangère sur l’ID du capteur


