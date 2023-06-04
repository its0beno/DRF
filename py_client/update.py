import requests

endpoint = 'http://localhost:8000/api/products/1/update/'


data={
    'title':'changed this ',
    'price': 29
}
get_requests = requests.put(endpoint,json = data)
print (get_requests.text)