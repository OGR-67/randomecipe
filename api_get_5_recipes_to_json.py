import requests

url = "https://themealdb.p.rapidapi.com/randomselection.php"

headers = {
    "X-RapidAPI-Key": "faf665f2b9msh45eb67b090b9ceep1c082cjsnca0b910f3aa3",
    "X-RapidAPI-Host": "themealdb.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.content

with open('data.json', 'wb') as f:
    f.write(data)
