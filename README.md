# ascii-art-anime
*Projet réalisé en 2 jours (2 fois 6h environ) avec des enfants de 10 à 12 ans. Ce Readme reprend la fiche pédagogique associée à ce projet.*

Apprendre à programmer les différentes méthodes de création de dessin n’utilisant que les caractères du clavier. Utiliser ces méthodes pour générer ses propres dessins et les animer en programmant avec le langage Python.

# Âge : +10 ans

# Temps : 2 jours

# Prérequis : aucun

# Notions :

- Programmation de base (variables, conditions, boucles) ;
- Caractères, chaîne de caractère et caractères d’échapement ;
- Listes ;
- Découverte du Terminal.

# Fonctionnalités :

- Afficher la liste des dessins disponibles dans la bibliothèque.
- L’utilisateur entre le nom d’un dessin dans le Terminal.
- Le dessin s’affiche et s’anime dans le Terminal

# Déroulement

- Jour 1 :
    - Introduction à l’ASCII et l’ASCII art
        - Qu’est-ce qu’un caractère ? Qu’est-ce qu’une chaîne de caractère ?
        - Qu’est-ce que le code ASCII ?
        - Comment faire du dessin avec des caractères ?
    - Introduction aux chaînes de caractères en Python :
        - Stocker des caractères dans une variable et imprimer cette variable dans le terminal
            
            `x = "laureline"
            print(x)`
            
        - Faire un input et l’afficher
        - Différencier les types avec input (entre un `int` dans un `str`)
        - Stocker plusieurs données dans une variable et l’imprimer
            
            `x = ["laureline", "chat"]
            print(x)`  // ça ne s'affiche pas bien T-T
            
        - Réaliser une boucle pour afficher la varaible
            
            `for mot in x:
                 print(mot)
            for index in range(2):
                 print(x[index])` //Ca marche mieux ces deux façons de faire !
            
        - Réaliser une boucle pour déplacer le curseur du terminal et réécrire une donnée par dessus
    - Programmer de l’ASCII art
        - Utilisation d’un second fichier `modeles.py` pour stocker les dessins
        - Écrire la première lettre de son prénom avec la lettre en question (puis toutes les lettres si en avance) en ASCII art et la stocker dans une variable
        - Afficher dans le terminal

- Jour 2 :
    - Recopier des dessins contenant plusieurs frames et les afficher à la suite dans le terminal
    - Effacer et réécrire sur un dessin
    - Calculer le modulo (reste d'une division euclidienne) permettant de connaître la frame à afficher
    - Fabriquer ses propres ASCII art
        - Sur papier
        - ASCII art sans mouvement
        - ASCII art avec mouvement
     - Programmer ses propres ASCII art animés

# Évaluation :

Obtenir au moins deux dessins d’au moins deux frames dans la bibliothèque qui peuvent s’animer dans le Terminal.

# Retours :

Très bons. Pas de difficulté à jongler entre les deux fichiers. Pour beaucoup, du mal à comprendre le fonctionnement de liste de listes pour mettre plusieurs frames pour un même dessin. Mieux insiter la prochaine fois. Les plus avancés ont pu créer plus de dessins ou les améliorer pendant que je réexpliquais et déboguais ceux qui en avaient besoins.

---

# Ressources :

Wiki ascii : [https://en.wikipedia.org/wiki/ASCII_art](https://en.wikipedia.org/wiki/ASCII_art)

Lib sys : [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)

Ecrire sur plusieurs lignes dans un terminal : [https://stackoverflow.com/questions/6840420/rewrite-multiple-lines-in-the-console](https://stackoverflow.com/questions/6840420/rewrite-multiple-lines-in-the-console)

Idées de dessins : [https://www.asciiart.eu/](https://www.asciiart.eu/animals/cats)
