#########################################################################################

Appname: Checkers
Developer: Robert Stuart
Developed for: CMPUT 355 Assignment 4 (University of Alberta)
Dependencies: pygame (pip install pygame)

Description:

This app is a basic Visualizer/Player for the game of Checkers. To start the game,
execute the python3 file run.py. This can typically be achieved by running the 
command "python3 run.py" or "run.py" from the directory it is
stored in. Note, all files must be present in the directory with run.py, especially
the CONFIG.txt file, the config.py file, and the app directory. Which command you 
use to launch the add depends on the setup of your indiviaul machine. 

Checkers Rules:

The game involves two players playing the game of checkers, taking turns making moves.

The game begins on blacks turn and players then alternate by moving pieces one space
diagonally. 

If an opponents piece occupies the space directly in the path of a players piece, 
and the subsequent space following the opponents piece is empty, a player may "jump" 
the opponents piece, capturing it and removing it from play. 

Typically after one move it would become the other players turn. However, in the case 
of a capture, if another capture is possible with the same piece the player may do so. 
Alternatively, they can choose to end their turn. No other pieces can be moved in this 
situation, only the initial piece used to capture. 

Initially players may only move in the direction directly away from their starting side. 
However, if a player manages to reach their opponents side that piece becomes a "king" 
designated by the letter "K" and may movein both directions. 

The game ends when one player has cleared the board of the opponentspieces, or the opponent 
forfeits. 

References:

Pygame was used in the development of this app. More information on pygame can be found
at: https://www.pygame.org/news
Documentation was referened in the development of this app at: https://www.pygame.org/docs/

#########################################################################################
