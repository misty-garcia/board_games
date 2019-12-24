import pandas as pd 
import numpy as np 
import re

import requests 
from bs4 import BeautifulSoup
import time

import os
import json


def scrape_one_game(url):
    """
    Scrape the boardgamegeek api for a single game
    """
    # requesting access to api
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
    
    designer = soup.find("link", attrs={'type':"boardgamedesigner"})
    designer = designer['value'] if designer else 'None'

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
    "category" : category,
    "mechanic" : mechanic,
    "publisher" : publisher,
    "description" : description,
}


def scrape_search(page):
    """
    Scrape the browsing page of boardgamegeek for the top games. Find id of each game and call scrape_single_game to retrieve remaining parameters.
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
        
        # pull remaining stats on browse page
        rank = soup.find_all("td", class_="collection_rank")[x-1].a["name"]
        geek_rating = soup.find_all('td', class_="collection_bggrating")[3*(x-1) + 0].text
        avg_rating = soup.find_all('td', class_="collection_bggrating")[3*(x-1) + 1].text
        votes = soup.find_all('td', class_="collection_bggrating")[3*(x-1) + 2].text
        
        # create dictionary
        search_page = {
            'name_clean' : name_clean,
            'rank' : rank,
            'geek_rating' : geek_rating, 
            'avg_rating' : avg_rating,
            'votes' : votes
        }
        
        # pull stats as dictionaty from api page for the currently selected game
        url = "https://www.boardgamegeek.com/xmlapi2/thing?id={}".format(link_id)
        print(link_id)
        single_page = scrape_one_game(url)
        
        # combine dictionaries into one
        search_page.update(single_page)

        # update games list
        games.append(search_page)

        # scraping count
        print('the following rank has just been pulled', rank)
    return games


def get_games():
    # check for presence of the file or make a new request
    filename = 'data1.txt'
    
    if os.path.exists(filename):
        print('data1.txt already exists')
    else:
        data = acquire.scrape_search(1)
        for count in range (2,11):
            data.extend(acquire.scrape_search(count))
        with open('data1.txt', 'w') as outfile:
            json.dump(data, outfile)

    # check for presence of the file or make a new request
    filename = 'data2.txt'
    
    if os.path.exists(filename):
        print('data2.txt already exists')
    else:   
        data = acquire.scrape_search(11)
        for count in range (12,21):
            data.extend(acquire.scrape_search(count))
        with open('data2.txt', 'w') as outfile:
            json.dump(data, outfile)
