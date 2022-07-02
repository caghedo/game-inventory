# game-inventory


Game-Inventory

These are instructions for the deployment of the game-inventory management system and how to use it afterwards. The game inventory system is very useful for keeping track of any games any accquintances/friends might have and whether they're installed or not. It follows a very simple 3 table structure, with one containing the list of Players, one containing the list of known Games, and the last one detailing the relationship of which players own what games, individually for each player, and each game. It is a many-to-many relationship that bonds these tables together.

Installation:
To install/deploy the Flask App, we're going to be using Jenkins. First, you need to turn on your VM. Then turn on Jenkins by typing the VM's external address in the bar followed by ":8080" afterwards (without the quotes). Then log into Jenkins, create a new project, and go to Configure. Where it says "Build commands", select execute shell, and type in the following:

#!/bin/bash
export ${DATABASE_URI}
export ${SECRET_KEY}
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 -m pytest --cov-report term-missing --cov=application tests/
python3 app.py

This is a script that will enable Jenkins to deploy not only the actual website itself, but the tests and databases along with it to make sure everything's running smoothly. The "create.py" only needs to be deployed once, so unless you want to delete the tables and all the data on them, get rid of this command on all subsequent builds. The app.py stays and so do the "pytest" reports. They are to detail how well the CRUD application is working. The exports are for the purpose of keeping certain variables secret and to avoid them being hard-coded into the app and away from prying eyes. The requirements.txt are there to give you everything you need to keep the app running and working as intended (Flask, sql_alchemy, pytests, etc...). The "/venv/bin/activate" is there to activate the virtual environment instead of using the VM's system bin, and keeping all your dependencies nice and seperated from any other Python projects you may have.

Now that Jenkins is running, you should be able to access it by either going to the VM's IP address in the browser bar and adding ":5000" to the end of it to access the game-inventory. Unfortunately for me, this method doesn't seem to work for me...yet. I have mainly accessed the website by going to the latest build, seeing the console output info, scrolling all the way to the bottom and pressing the first hyperlink, which then takes me to the website.

Usage:
The usage of the game-inventory system is very easy. You have a game you know, then add it to the Game list. Add as many as you want. Same goes for players. Any friends/family that you know game on Steam, add them to the Player list, and any games you know for certain a player has(but not neccesarily installed), you add to the Player_Game list. The Update link takes you to the Update seciton, where you can change the info of an entry in any of the aforementioned tables. The View link lets see all entries in the specific table, and the Create link lets you add an entry to the database. The Delete is self-explanatory, you don't want an entry, then delete it by pressing the button underneath it. One small thing to mention, if you delete any entries in the "Player" or "Game" section, then any entries tied to them in the "Player_Game" table via foreign keys also get deleted in order to ensure there is no uselsss information.



All credits go to Chris Aghedo. Heh.

