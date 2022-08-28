import requests

url = "https://random-recipes.p.rapidapi.com/ai-quotes/5"

headers = {
    'x-rapidapi-host': "random-recipes.p.rapidapi.com",
    'x-rapidapi-key': "faf665f2b9msh45eb67b090b9ceep1c082cjsnca0b910f3aa3"
}

response = requests.get(url, headers=headers)
data = response.content

with open('data.json', 'wb') as f:
    f.write(data)
