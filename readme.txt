This file is intended to keep track of the plans for this project and any relavant notes

1) Plan is to create a web app to interact with a database containing soccer players and
teams in order to provide insights for team managers or interested fans on how to build
a better team to compete in the main leagues of professional European soccer.

2) If you are struggling with accessing the files and setting up a virtual Python environment
please refer to https://iu.instructure.com/courses/2061671/pages/webapp-materials?module_item_id=26424023
the week 8 web app materials module where the video on Flask goes through how to set up VS Code
and how to establish a virtual python environment for this project.

3) Datasets for importing:
The plan is to download the following datasets and complile them to create a database to accomplish
the project goals. The following datasets are uploaded to the git project folder:
	a) teams_fifa22.csv(teams) - https://www.kaggle.com/datasets/cashncarry/fifa-22-complete-player-dataset
		-Team statistics from FIFA 22 video game
	b) players_fifa22.csv(plyr_atr) - https://www.kaggle.com/datasets/cashncarry/fifa-22-complete-player-dataset
		-Player attribute ratings from FIFA 22 game
	c) league.csv(league) - https://www.kaggle.com/datasets/jehanbhathena/big-5-european-football-leagues-stats/download
		-Team stats from big 5 European soccer leagues
	d) plyr_stat.csv(plyr_stat) - https://www.kaggle.com/datasets/shushrutsharma/top-5-football-leagues/download
		-Player statistics data from big 5 European soccer league
	e) plyr_shot.csv(plyr_shot) - https://www.kaggle.com/datasets/shushrutsharma/top-5-football-leagues/download

4)DB design plan:
	a)Create sqlite database with each csv file imported as a table.
	b)Most datatypes should be either INTEGER, REAL or TEXT.
	c)Each table either has a column designated as primary key or if no columns contain all unique values, an index is 
	set in the creation of the table.

