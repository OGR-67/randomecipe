from distutils.command.config import config
import requests
import os
from django.core.management.base import BaseCommand
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Get 5 random recipes from API and save them to data.json'

    def handle(self, *args, **kwargs):
        url = "https://themealdb.p.rapidapi.com/randomselection.php"

        headers = {
            "X-RapidAPI-Key": "faf665f2b9msh45eb67b090b9ceep1c082cjsnca0b910f3aa3",
            "X-RapidAPI-Host": "themealdb.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        data = response.content

        with open(os.path.join(BASE_DIR, 'data.json'), 'wb') as f:
            f.write(data)

        self.stdout.write(
            "Work done!\n\
            Enjoy your food ;)"
        )
