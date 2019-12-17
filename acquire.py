import pandas as pd 
import numpy as np 

import requests 
from bs4 import BeautifulSoup

def scrape_one_game(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    name = soup.find('name').get('value')
    year = soup.find("yearpublished").get('value')
    min_players = soup.find("minplayers").get('value')
    max_players = soup.find("maxplayers").get('value')
    min_time = soup.find("minplaytime")['value']
    max_time = soup.find("maxplaytime")['value']
    description = soup.find("description").text
    designer = soup.find("link", attrs={'type':"boardgameartist"})['value']

    tags = soup.find_all("link", attrs={'type':'boardgamecategory'})
    category = []
    for tag in tags:
        category.append(tag['value'])

    tags = soup.find_all("link", attrs={'type':'boardgamemechanic'})
    mechanic = []
    for tag in tags:
        mechanic.append(tag['value'])

    tags = soup.find_all("link", attrs={'type':'boardgamepublisher'})
    publisher = []
    for tag in tags:
        publisher.append(tag['value'])

    return {
    "name" : name,
    "year" : year,
    "min_players" : min_players,
    "max_players" : max_players,
    "min_time" : min_time,
    "max_time" : max_time,
    "designer" : designer,
    "family" : category,
    "mechanic" : mechanic,
    "publisher" : publisher,
    "description" : description,
}

