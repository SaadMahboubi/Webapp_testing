
# Ds ce script, ns testons la perf de la route "./regsiter"

# https://www.blazemeter.com/blog/how-to-run-locust-with-different-users

# locust -f ./tests/performance_tests/locust3_login --host http://127.0.0.1:5000 --users 1 --spawn-rate 1
# Regarder l'onglet Statistics de http://localhost:8089


from locust import HttpUser, task, between
from locust.user import wait_time
import json

class PerfTest(HttpUser):
    wait_time = between(1, 5)

    @task
    def registerPerf(self):
        # self.client.get((url="/register")
        payload = {"name":"name", "email":"email@email.com", "password":"password"}
        # self.client.post(url="/register", data=json.dumps(payload))
        self.client.post("/register", data=payload)