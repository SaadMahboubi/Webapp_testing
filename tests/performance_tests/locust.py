from locust import HttpUser, TaskSet, task, between
from server import *
# locust -f ./tests/performance_tests/locust.py --host http://127.0.0.1:5000 --users 500 --spawn-rate 500
# Regarder l'onglet Charts de http://localhost:8089

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def index_page(self):
        self.client.get(url='/')
        
    @task
    def user_login(self):
        data = {"email":"john@simplylift.co"}
        self.client.post("/showSummary",data)

    @task 
    def user_book(self):
        self.client.get(url='/book/Spring%20Festival/Simply%20Lift')

    @task
    def test_page(self):
        self.client.get(url='/score')
        
    @task
    def test_page(self):
        self.client.get(url='/purchasePlaces',data =dict(club = 'Simply Lift', competition='Spring Festival', places = 1))
        
    @task
    def test_page(self):
        self.client.get(url='/logout')