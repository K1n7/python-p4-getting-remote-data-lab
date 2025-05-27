import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text  # returns raw response body as a string

    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # returns JSON as dict or list
