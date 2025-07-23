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

    def print_board(self, show_ships=True):
        """
        This function prints the game board.
        """
        print("  " + "  ".join(str(i) for i in range(self.size))) # Print column headers
        for i, row in enumerate(self.grid): # Print each row with row index
            print(i, " ".join(row))

    def place_ships(self):
        """
        This function places ships randomly on the board.
        """
        self.ship_locations = [] # Reset ship locations
        for _ in range(self.num_ships):
            while True:
                ship_row = random.randint(0, self.size - 1) # Randomly select a row
                ship_col = random.randint(0, self.size - 1) # Randomly select a column
                ship_coords = (ship_row, ship_col) # Tuple to represent ship coordinates
                if ship_coords not in self.ship_locations: # Check if the ship is already placed
                    self.ship_locations.append(ship_coords) # Place the ship
                    self.grid[ship_row][ship_col] = "🚢" # Mark the ship
                    break
        print("Ships placed at:", self.ship_locations) # Debugging statement to show ship locations


board = Board(5)  # Create a board of size 5
board.place_ships()  # Place ships on the board
board.print_board()  # Print the initial board
