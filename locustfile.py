from locust import HttpUser, task
import json


class UserBehavior(HttpUser):

    def __init__(self, parent):
       super(UserBehavior, self).__init__(parent)

       self.token = ""
       self.headers = {}
       self.product_request = None

    def read_file(self):
       with open("product-req.json", 'r', encoding='utf8') as f:
            data = f.read()
            self.product_request = json.loads(data)
      

    def on_start(self):
      self.read_file()
      self.headers = {'Authorization': 'Bearer ' + self.token, "Content-Type": "application/json; charset=utf8", "Accept": "application/json"}

    @task(1)
    def index(self):
        print(self.product_request)
        self.client.post("/api/v1/product-requests", json=self.product_request, headers=self.headers)

