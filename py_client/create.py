import requests

endpoint = 'http://localhost:8000/api/products/'

get_requests = requests.post(endpoint, json = {'title': "Name", "content":"this is content", "price": 12})
print (get_requests.text)