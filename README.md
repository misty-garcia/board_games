## What makes a quality board game? 

Due to my love of board games, I've decided to try and determine what makes a board game well liked. BoardGameGeek.com (bgg) is the ultimate resourse for all things board games. Thousands on users rate each game and this rating will be used to determine game quality. 

Goal: Practice my data science skills and find cool board game insights

### Acquire
Dataset built by web scraping BoardGameGeek's api and search engine for the top 2000 games. [Access the csv file here.](https://drive.google.com/file/d/1akXzg_fbt3ULhH1wnNTee32rftM-0-Rq/view?usp=sharing)

**Data Dictionary**
- rank: the ranked position of a game based on the game's geek_rating
- name_clean: the name pulled from the search page
- geek_rating: the avg_rating with an added "weight" to pull games with few ratings towards a middle ranking
- avg_rating: the average rating from all registered bgg users
- votes: the number of votes each board game has
- name: the board game name pulled from the api
- year: the year the game was released
- min_players: the minimum number of players that can play
- max_players: the maximum number of players that can play
- min_time: the minimum time to play (minutes)
- max_time: the maximum time to play (minutes) *these times are always lies*
- designer: the primary designer of the game
- categories: a list of categories that the game falls into
- mechanic: a list of mechanics the game utilizes
- publisher: a list of publishers for the game
- description: a description that provides a general overview of the game



