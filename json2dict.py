import json
from recipe.models import Recipe


with open('data.json') as json_file:
    data = json.load(json_file)

    print(data[0])