import requests

endpoint = 'http://localhost:8000/api/products/4/delete'

get_requests = requests.delete(endpoint)
print (get_requests.text)