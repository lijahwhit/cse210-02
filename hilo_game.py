# Title: Hilo Game - W03 Prepare: Articulate
# Authors:
# Class: CSE 210 Programming with Classes


import random


class Hilo:

    def __init__(self):
        self.score = 0

    def start(self):
        """Description: starts a new game
        """

        # set initial parameters for new game

        while True:
            # game play

            print()

        # when the game loop is broken, start a new game
        self.start()


def main():
    """Description: initializes the game
    """
    print(f"Welcome to Hilo!\n")
    # create the game object
    game = Hilo()
    # start the game
    game.start()


if __name__ == "__main__":
    main()
