## What makes a quality board game? 

Due to my love of board games, I've decided to try and determine what makes a board game well-liked. BoardGameGeek.com (BGG) is the ultimate resourse for all things board games. Thousands of users rate each game and this rating will be used to determine game quality. 

Goal: Practice my data science skills and find cool board game insights

BGG is home is 112,801 board games. Currently, 18,330 board games are ranked. For this analysis, the top 2,000 board games are analyzed, which is about the top 11% of ranked games. 

Dataset was built by web scraping the browse page for the top games and then utilizing BoardGameGeek's api to pull the respective parameters for each game. The data was downloaded Dec 30th, 2019. Access data used in this analysis: 

[Games 1 - 1000](https://drive.google.com/file/d/1NTxq3Oe0KDT-lKvuwgMhWbXyyhr-AzKr/view?usp=sharing)

[Games 1001 - 2000](https://drive.google.com/file/d/1CfV9Z7RMtDl0V4FJENq5IwXxxoFF4Hn1/view?usp=sharing)


**Data Dictionary**
- name_clean: the name pulled from the browse page
- rank: the ranked position of a game based on the game's geek_rating
- name: the board game name pulled from the api
- year: the year the game was released
- min_players: the minimum number of players that can play
- max_players: the maximum number of players that can play
- min_time: the minimum time to play (minutes)
- max_time: the maximum time to play (minutes) *these times are always lies*
- designer: a list of  designers for the game game
- category: a list of categories that the game falls into
- mechanic: a list of mechanics the game utilizes
- publisher: a list of publishers for the game
- description: a description that provides a general overview of the game
- num_votes: the number of votes each board game has
- avg_rating: the average rating from all registered bgg users
- geek_rating: the avg_rating with an added "weight" to pull games with few ratings towards a middle ranking
- complexity: the complexity of the game based on a scale of 1-5 



