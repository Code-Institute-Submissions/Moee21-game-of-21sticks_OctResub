# 21 MatchSticks Game

21 MatchSticks is a Python terminal game,which runs on Heroki.

Users can try to beat the computer by picking numbers from one to four at each round and only can win if the users are kept from the last stick.

[Here is the live version of my project](https://game-of-21sticks.herokuapp.com/)

<img src ="assets/images/am%20i%20responsive%20image.png" width ="600">

![](vscode-remote://moee21-gameof21sticks-vy2ku7asxtc.ws-eu72.gitpod.io/workspace/game-of-21sticks/assets/images/am%20i%20responsive%20image.png)

## How to play
#

* There are 21 matchsticks.
* The computer asks the player to pick 1, 2, 3, or 4     matchsticks.
* After the person picks, the customer does its picking.
* Whoever is forced to pick up the last matchstick loses the game.

## Features
#

<img src ="assets/images/start%20of%20the%20game.png" width="600">

![](vscode-remote://moee21-gameof21sticks-vy2ku7asxtc.ws-eu72.gitpod.io/workspace/game-of-21sticks/assets/images/start%20of%20the%20game.png)

* The player will not see what number the computer picks.

<img src ="assets/images/play%20against%20the%20computer.png" width ="600">

![](vscode-remote://moee21-gameof21sticks-vy2ku7asxtc.ws-eu72.gitpod.io/workspace/game-of-21sticks/assets/images/play%20against%20the%20computer.png)

* Play against the computer
* Accepts user input

<img src ="assets/images/entering%20some%20incorrect%20data%20twice.png" width ="600">

![](vscode-remote://moee21-gameof21sticks-vy2ku7asxtc.ws-eu72.gitpod.io/workspace/game-of-21sticks/assets/images/entering%20some%20incorrect%20data%20twice.png)

* Input validation and error-checking
   * The user must enter values ranging between 1-4. if the user enters any value less than 1 or greater than 4 then a message is displayed: invalid input and again the input is taken from user ranging between 1-4.
   * The user must enter only int value. if the user enters some string either empty or with some value, then a message 'you can only enter numeric values' is displayed and the input is taken again from the user.

## Testing
#
I have manually tested this project by:
  * Passed the code through https://www.pythonchecker.com/ and confirmed there are no problems.

## Validator Testing
#
  * pythonchecker
    * No errors were returned from https://www.pythonchecker.com/

## Deployment 
#
 * Steps for deployment:
   * Fork or clone this repository
   * Create a new Heroku app
   * Set the buildbacks to Python and NodeJS in that order
   * Link the Heroku app to the repository
   * Click on Deploy

## Credits 
#
  * Code Institute for the deployment terminal
  * The idea and inspiration to make this game was taken from:
https://www.youtube.com/watch?v=ReQz7vwDjPs&ab_channel=NickyDylewski
https://www.youtube.com/watch?v=SdrSEq_dsBU&t=326s&ab_channel=3ATeam

