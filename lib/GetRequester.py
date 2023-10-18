import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response=requests.get(self.url)
        return response.content

    def load_json(self):
        response=json.loads(self.get_response_body())
        return response
        

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
hey=get_requester.load_json()
print(json.dumps(hey,indent=4,sort_keys=True))