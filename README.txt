#########################################################################################

Appname: Checkers
Developer: Robert Stuart
Developed for: CMPUT 355 Assignment 4 (University of Alberta)
Dependencies: pygame (pip install pygame)

Icon made by Freepik (https://www.flaticon.com/authors/freepik) from Flaticon (https://www.flaticon.com/)

Description:

This app is a basic Visualizer/Player for the game of Checkers. To start the game,
execute the python3 file run.py. This can typically be achieved by running the 
command "python3 run.py" or "run.py" from the directory it is
stored in. Note, all files must be present in the directory with run.py, especially
the CONFIG.txt file, the config.py file, and the app directory. Which command you 
use to launch the add depends on the setup of your indiviaul machine. 

Checkers Rules:

The game begins with Black to play.
Players take turns moving their stones in one of two possible ways.

1: A player may move their stone diagonally one space so long as that space is empty and the 
direction is valid

2: A player may "capture" an opponents stone given the opponents stone occupies a valid move 
space and the subsequent space is empty.

The direction a player may move is initially toward the opponents side. 

If a player manages to get one of their stones across the board to the first row of the opponents 
side, that stone becomes a "king" and can now move in both directions.

In the case that a players stone captures an opponents stone, if that stone can immidiately capture 
another stone it may do so (this rule can stack for tripple and large captures)

When a double (or higher) capture is possible, the capturing stone remains selected. If the player 
would like to end their turn and not capture again they simply click the stone again to end their turn. 

The game ends when one player has captured all of the opponents stones, or a player concedes on their 
turn.

References:

Pygame was used in the development of this app. More information on pygame can be found
at: https://www.pygame.org/news
Pygame license can be found at: https://www.pygame.org/docs/LGPL.txt
Documentation was referened in the development of this app at: https://www.pygame.org/docs/

#########################################################################################
