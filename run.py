import random # Importing the random module

class Board:
    """
        A class representing the game board for battleship with a constructor, print_board, place_ships, check_hit, all_ships_sunk functions.
    """
    def __init__(self, size):
        """
        Constructor to initialize the game board with a given size and place ships randomly.
        """
        self.size = size # Size of the board
        self.grid = [] # 2D list to represent the board
        for _ in range(size): # Initialize the board with water
            self.grid.append(["🌊"] * size)
        self.num_ships = 5 # Number of ships to place
        self.ship_locations = [] # List to store ship locations
        self.hits = [] # List to store hit locations
        self.guesses_made = [] # List to store guesses made by the player

    def print_board(self):
        """
        This function prints the game board.
        """


