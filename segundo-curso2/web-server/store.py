import requests

def get_categories():
  response = requests.get('https://api.escuelajs.co/api/v1/products')
  print(response.status_code)
  print(response.text)
  print(response.json())
  categorias = response.json()
  for categoria in categorias:
    print(categoria['title'])
  return response.json()
  