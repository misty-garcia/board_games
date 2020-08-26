import pandas as pd 
import numpy as np 
import re

import requests 
from bs4 import BeautifulSoup
import time

import os
import json


def scrape_game_api(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")

    # pull parameters for a single game
    name = soup.find('name').get('value')
    year = soup.find("yearpublished").get('value')
    min_players = soup.find("minplayers").get('value')
    max_players = soup.find("maxplayers").get('value')
    min_time = soup.find("minplaytime")['value']
    max_time = soup.find("maxplaytime")['value']
    description = soup.find("description").text

    # pull all designers 
    tags = soup.find_all("link", attrs={'type':"boardgamedesigner"})
    designer = []
    if designer != None:
        for tag in tags:
            designer.append(tag['value'])

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

    # pull stats
    num_votes = soup.find('usersrated')['value']
    avg_rating = soup.find('average')['value']
    geek_rating = soup.find('bayesaverage')['value']
    complexity = soup.find('averageweight')['value']
    rank = soup.find('rank')['value']

    # return a dictionary of all pulled values
    return {
    "rank" : rank,
    "name" : name,
    "year" : year,
    "min_players" : min_players,
    "max_players" : max_players,
    "min_time" : min_time,
    "max_time" : max_time,
    "designer" : designer,
    "category" : category,
    "mechanic" : mechanic,
    "publisher" : publisher,
    "description" : description,
    "num_votes" : num_votes,
    "avg_rating" : avg_rating,
    "geek_rating" : geek_rating,
    "complexity" : complexity,
    }


def scrape_search(page):
    """
    Scrape the browsing page of boardgamegeek for the top games. Find id of each game and call scrape_game_api to retrieve parameters.
    """
    # initialize games list
    games = []

    # scrape browsing page 
    url = "https://boardgamegeek.com/browse/boardgame/page/{}".format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    
    # loop through the hundred games on a single page   
    for x in range(1,101):
        time.sleep(5)
        # pull and clean name to compare later
        name = soup.find('div', id='results_objectname{}'.format(x)).text
        name_clean = re.sub(r'\n+(.+)\n.*\n',r'\1', name)
        
        # pull link id to retrieve stats from api
        link = soup.find('div', id='results_objectname{}'.format(x)).a['href']
        link_id = re.sub(r'.*/(\d+)/.*', r'\1', link)

        rank = soup.find_all("td", class_="collection_rank")[x-1].a["name"]
                
        # create dictionary
        search_page = {
            'name_clean' : name_clean,
        }
        
        # pull stats as dictionary from api page for the currently selected game
        url = "https://www.boardgamegeek.com/xmlapi2/thing?id={}&stats=1".format(link_id)
        print('game id', link_id)
        parameters = scrape_game_api(url)
        
        # combine dictionaries into one
        search_page.update(parameters)

        # update games list
        games.append(search_page)

        # scraping count
        print('the following rank just been pulled:', rank)
    return games


def get_games(thousands):
    for x in range(thousands):
        # establish file name of 1000 entries & and first page
        filename = 'data_' + str(x+1) + '000.txt'
        first_page = x*10+1

        if os.path.exists(filename): #check is file already exists
            print(filename + ' already exists')
        else:
            data = scrape_search(first_page)
            for count in range (first_page+1,first_page+10):
                data.extend(scrape_search(count))
            with open(filename, 'w') as outfile:
                json.dump(data, outfile)
