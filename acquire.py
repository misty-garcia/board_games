import pandas as pd 
import numpy as np 
import re

import requests 
from bs4 import BeautifulSoup


def scrape_one_game(url):
    """
    Scrape the boardgamegeek api for a single game
    """
    # requesting access to api
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")

    # pulling parameters for a single game
    name = soup.find('name').get('value')
    year = soup.find("yearpublished").get('value')
    min_players = soup.find("minplayers").get('value')
    max_players = soup.find("maxplayers").get('value')
    min_time = soup.find("minplaytime")['value']
    max_time = soup.find("maxplaytime")['value']
    description = soup.find("description").text
    designer = soup.find("link", attrs={'type':"boardgamedesigner"})['value']

    # pull all categories 
    tags = soup.find_all("link", attrs={'type':'boardgamecategory'})
    category = []
    for tag in tags:
        category.append(tag['value'])

    # pull all mechanics
    tags = soup.find_all("link", attrs={'type':'boardgamemechanic'})
    mechanic = []
    for tag in tags:
        mechanic.append(tag['value'])

    # pull all publishers
    tags = soup.find_all("link", attrs={'type':'boardgamepublisher'})
    publisher = []
    for tag in tags:
        publisher.append(tag['value'])

    # return a dictionary of all pulled values
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


def scrape_search():
    """
    Scrape the search page of boardgamegeek for the top games. Find id of each game and call scrape_single_game to retrieve remaining parameters.
    """
    url = "https://boardgamegeek.com/browse/boardgame/page/1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    
    games = []
    for x in range(1,101):
        name = soup.find('div', id='results_objectname{}'.format(x)).text
        name_clean = re.sub(r'\n+(.+)\n.*\n',r'\1', name)
        
        link = soup.find('div', id='results_objectname{}'.format(x)).a['href']
        link_id = re.sub(r'.*/(\d+)/.*', r'\1', link)
        
        rank = soup.find_all("td", class_="collection_rank")[x-1].a["name"]
        geek_rating = soup.find_all('td', class_="collection_bggrating")[3*(x-1) + 0].text
        avg_rating = soup.find_all('td', class_="collection_bggrating")[3*(x-1) + 1].text
        votes = soup.find_all('td', class_="collection_bggrating")[3*(x-1) + 2].text
        
        search_page = {
            'name_clean' : name_clean,
            'rank' : rank,
            'geek_rating' : geek_rating, 
            'avg_rating' : avg_rating,
            'votes' : votes
        }
        
        url = "https://www.boardgamegeek.com/xmlapi2/thing?id={}".format(link_id)
        single_page = scrape_one_game(url)
        
        search_page.update(single_page)
        games.append(search_page)
        print('the following rank has just been pulled', rank)
    return games