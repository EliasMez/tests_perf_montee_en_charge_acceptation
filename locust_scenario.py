from locust import HttpUser, task, between
from items_api import Item

class MonScenario(HttpUser):
    host = "http://127.0.0.1:8000" 
    wait_time = between(1, 5)

    @task
    def acceder_page_web(self):
        self.client.get("/items")
    
    @task
    def soumettre_formulaire(self):
        data = {'name':"test", 'description':"test"}
        self.client.post("/items", json=data)