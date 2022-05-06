# Title: Hilo Game - W03 Prepare: Articulate
# Authors:
# Class: CSE 210 Programming with Classes


import random


class Card:

    def __init__(self):
        self.number = 0

    def randomize(self):
        self.number = random.randrange(1, 14)


class Hilo:

    def __init__(self):
        self.score = 0
        self.card = Card()

    def start(self):
        """Description: starts a new game
        """

        # set initial parameters for new game
        self.score = 300

        while True:
            # game play
            self.card.randomize()

            print(f"The current card is: {self.card.number}")

            user_input = input("choose Y/N")

            if(user_input == "N"):
                break

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
