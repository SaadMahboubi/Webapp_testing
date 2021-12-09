# Projet Web App

## Contexte : 
En arrivant à notre bureau un matin, nous recevons le mail suivant de Sayf Bejaoui :

A : vous
Sujet : FW : Construction de QA v0.9.1

Je viens de recevoir le rapport de QA pour la phase 1 du projet. Il y a plusieurs bugs qui font planter la WebApp (maintenant de plus en plus populaire) : plateforme numérique pour coordonner les compétitions deadlifting, strongman en Amérique du Nord et en Australie ! Malheureusement, je ne serai pas au bureau pour les prochains jours (un de mes enfants est tombé malade). Voici le travail demandé : 

Vous installeriez pytest (notre framework de test préféré) et Locust (tests de performance). Je vous encourage à adopter une approche de TDD, car cela vous aidera à rationaliser votre travail.
J'ai déjà listé les bugs de la phase 1 que vous devriez régler et mettre en œuvre les éléments de la phase 2 (voir ci-dessus). Très important : Essayez de reproduire les bugs sur votre machine pour mieux les comprendre et ainsi plus facilement les résoudre. 
Vous testeriez de manière approfondie les résultats requis pour toutes les fonctionnalités (de la WebApp). A noter que pour éviter d'utiliser une DB, nous passons par un fichier JSON.
Vous prépareriez un rapport de test et un rapport de performances, conformément au Guide de dév de l’entreprise car le QA nous reproche de ne pas respecter les normes.
Par ailleurs, je vous préviens : l'équipe commerciale n'était pas sûre du nombre de points à attribuer par concours, vous devrez donc certainement ajuster cela plus tard. Pour l'instant, il suffit de s'en tenir à 1 point = 1 concours. Je vais demander à Zayn, le Product Owner, de vous le confirmer (email de Zayn : vous demandant de modifier plus tard cette fonctionnalité). 

Une fois que vous aurez terminé, nous ferons un examen de ce que vous avez dans la branche QA du code. 

Nous examinerons les rapports et la manière dont vous avez résolu les problèmes, nous examinerons votre code et nous testerons la couverture de la nouvelle fonctionnalité. 
Merci ! 

Sayf Bejaoui,


## Exécution de l'application : 
    python server.py puis accéder à http://127.0.0.1:5000/

## Exécution de la vérification de la couverture des tests sur l'application server : 
    - coverage run -m pytest
    - coverage html (création du fichier html présent dans le dossier /htmlcov)

## Exécution des test de performances avec locust : 
    - locust -f ./tests/performance_tests/locust.py --host http://127.0.0.1:5000 --users 500 --spawn-rate 2
    - Regarder l'onglet Charts de http://localhost:8089
