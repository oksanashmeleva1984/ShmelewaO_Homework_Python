import os
import requests


class ProjectApiClient:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL", "https://ru.yougile.com")
        self.token = os.getenv("API_TOKEN", "")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        url = f"{self.base_url}/api-v2/projects"
        return requests.post(url, json=data, headers=self.headers)

    def get_project(self, project_id):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id, data):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.put(url, json=data, headers=self.headers)
