# Battleships Game

This Battleship is a one-player game where the player strategically guesses the locations of the computers's hidden ships on a grid, attempting to sink them before your own fleet is destroyed. The game, originally a pen-and-paper game, was popularized by Milton Bradley as a plastic board game in 1967. Players used pegs to mark hits and misses, aiming to be the first to sink all of their opponent's ships. Luckily, this version of the game is implemented in Python, allowing for a blazingly fast digital experience.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.
