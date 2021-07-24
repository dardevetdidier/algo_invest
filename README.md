# AlgoInvest&Trade
Recherche de solutions pour maximisation d'investissements

---

### Informations générales

Les algorithmes ont été développés avec Python 3.9.2.\
Les fichiers contenant les données à analyser sont présents dans le dépôt et ne doivent pas être renommés pour assurer 
le bon fonctionnement du programme.

Deux solutions sont présentées :
* solution force brute
* solution optimisée de programmation dynamique


### Comment exécuter les fichiers :

* Cloner ce dépôt avec la commande
  `$ git clone https://github.com/dardevetdidier/algo_invest.git`
  
  
* Créer un environnement virtuel : Depuis un terminal, accéder au répertoire racine du projet
et utiliser la commande :

    `$ python -m venv venv` 

  
* Activer l'environnement virtuel :

    `$ source venv/Scripts/activate` (Linux et Mac)\
    `$ venv\Scripts\activate.bat` (Windows)

  
* Pour exécuter le fichier bruteforce.py :
    * dans un terminal, accéder au répertoire racine `/algoinvest` et lancer la commande\
      ` $ python bruteforce.py`
  * Cet algorithme analysera les données du fichier `dataset0.csv` contenant 20 actions
    

* Pour exécuter le fichier optimized.py : 
    * dans un terminal, accéder au répertoire racine `/algoinvest` et lancer la commande\
      ` $ python optimized.py`
    * Le programme vous demandera de choisir les données à analyser :
        * 0 : `dataset0.csv` : 20 actions
        * 1 : `dataset1.csv` : 1001 actions
        * 2 : `dataset2.csv` : 1000 actions
    * Une fois le programme terminé, la solution est affichée dans la console et écrite 
      dans un fichier texte selon les données sélectionnées :
        * solution_dataset0.txt
        * solution_dataset1.txt
        * solution_dataset2.txt
