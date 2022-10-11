from locust import HttpUser, task
    
class DeliveryHero(HttpUser):
    @task
    def homepage(self):
        self.client.get("https://reqres.in/api/users?page=2", name="list users")
        self.client.get("https://reqres.in/api/users/2", name="single user")
        self.client.post("https://reqres.in/api/users",name="create user",json={"name":"mert","job":"testing"})
        self.client.patch("https://reqres.in/api/users",name="update user")
        self.client.delete("https://reqres.in/api/users",name="delete user")