# Title: Hilo Game - W03 Prepare: Articulate

# Authors: Elijah Whitchurch

# Class: CSE 210 Programming with Classes

Hilo Python Game README

Overview:

Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

Hilo is played according to the following rules:

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

DESIGN DOCUMENT:

We decided to have a main function that creates an instance of a "Hilo" class.
Within the Hilo class there are methods that start the game, and control the game logic in a loop.
It will create an instance of "Card" class, and call it's randomize method to get a random number to use in game.

Classes:

Hilo
attributes:
instance of card
score
methods:

- start game

Card
attributes: number
methods:

- randomize card

Other Methods:
Main
