from locust import HttpUser, task
import json


class UserBehavior(HttpUser):

    def __init__(self, parent):
       super(UserBehavior, self).__init__(parent)

       self.token = "eyJhbGciOiJIUzUxMiJ9.eyJvcmdhbml6YXRpb25faW4iOiI4OTA5MDUzNTA5MDEiLCJpc19yZWZyZXNoX3Rva2VuIjp0cnVlLCJ0b2tlbl9leHBpcmF0aW9uX2RhdGUiOjE2MDk3NTIzNDU3MjUsImV4cCI6MTYwOTc1MjM0NSwiZW1wbG95ZWVfaW4iOiI4NzkwNjU3ODQzMjEiLCJ1c2VybmFtZSI6Im1lbjFAbWVuMSIsInRva2VuX2NyZWF0ZV9kYXRlIjoxNjA3MDczOTQ1NzI1fQ.MuNqK2NkGVGl3J7xCZdPbqYRP9t1Og-xuDV4awD6DpHKDFw_Pue87TYHt2Pmy9tCSHzayE4Uj5ffZfHoh5zoDg"
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

