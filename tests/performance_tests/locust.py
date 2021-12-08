from locust import HttpUser, TaskSet, task, between
import time 
from server import *

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def index_page(self):
        self.client.get(url='/')
        
    @task
    def test_page(self):
        self.client.post(url='/showSummary')

    @task
    def test_page(self):
        self.client.get(url='/book/<competition>/<club>')
        
    @task
    def test_page(self):
        self.client.get(url='/purchasePlaces')
        
    @task
    def test_page(self):
        self.client.get(url='/logout')