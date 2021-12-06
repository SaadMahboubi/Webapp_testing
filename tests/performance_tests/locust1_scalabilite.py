
# Q : Comment la WebApp se comporte en termes de perf face à une augmentation accrue du nb d'User ?
# Ds ce script, ns montrons que le temps de réponse reste constant malgré le fait que le nb d'User augmente (d'une façon exceptionnelle)
# C'est le schéma idéal

# locust -f ./tests/performance_tests/locust1_scalabilite.py --host http://127.0.0.1:5000 --users 500 --spawn-rate 500
# Regarder l'onglet Charts de http://localhost:8089



# La classe HttpUser est une instance de HttpSession qui fournit un client de test. 
# Comme pour les unit tests, le client permettra de faire la requête sur l’URL de votre choix.

# Autrement dit, lorsqu'un test démarre, Locust créera une instance de cette classe pour chaque User qu'il simule, et chacun de ces Users s'exécutera dans son propre thread.

# Vs pouvez maintenant implémenter votre scénario dans une méthode précédée par le décorateur @task. En effet, Locust considère que chaque méthode contenant @task est une tâche à lancer.

from locust import HttpUser, task, between
from locust.user import wait_time

class PerfTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def slow_page(self):
        self.client.get(url="/http://127.0.0.1:5000/")