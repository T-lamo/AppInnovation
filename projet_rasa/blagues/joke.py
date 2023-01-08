import requests

def get_joke():
  url = "https://blague.xyz/api/joke/random"
  headers = { "Accept": "application/json" }
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    joke = response.json()["joke"]
    return str(joke["question"]) +" "+ str(joke["answer"])
  else:
    return None
