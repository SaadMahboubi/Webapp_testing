
# Ds ce script, ns montrons la différence entre les temps de réponse de 2 routes : une lente (en moy. 2s de latence) et une rapide (en moy. 5ms) ?
# Ns avons en effet implémenté un time.sleep de 2s dans la roote /slow_page 
# Ns constatons que Locust retourne bien ces valeurs!  

# locust -f ./tests/performance_tests/locust2_quick_slow_page --host http://127.0.0.1:5000 --users 500 --spawn-rate 2
# Regarder l'onglet Statistics de http://localhost:8089


from locust import HttpUser, task, between
from locust.user import wait_time

class PerfTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def quick_page(self):
        self.client.get(url="/quick_page")

    @task
    def slow_page(self):
        self.client.get(url="/slow_page")        