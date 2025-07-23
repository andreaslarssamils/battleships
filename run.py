import random # Importing the random module

class Board:
    """
        A class representing the game board for battleship with a constructor, print_board, place_ships, check_hit, all_ships_sunk functions.
    """
    def __init__(self, size, num_ships=5):
        """
        Constructor to initialize the game board with a given size and place ships randomly.
        """
        self.size = size # Size of the board
        self.grid = [] # 2D list to represent the board
        for _ in range(size): # Initialize the board with water
            self.grid.append(["🌊"] * size)
        self.num_ships = num_ships # Number of ships to place
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

    def check_hit(self, row, col):

        """
        This function checks if a guess hits a ship.
        And returns "hit", "miss", "invalid" or "already guessed".
        """
        self.guesses_made.append((row, col)) # Add the guess to the list of guesses

        if (row, col) in self.ship_locations: # Check if the guess hits a ship
            if (row, col) not in self.hits:
                self.grid[row][col] = "💥" # Mark the hit
                self.hits.append((row, col))
                # print(f"Hit at ({row}, {col})!")
                if self.all_ships_sunk():
                    #print("All ships sunk! You win!")
                    return "All ships sunk! You win! 🎉"
                else:
                    # print(f"BOOOOM! Hit at ({row}, {col})!")
                    return "Ahay! Hiiiit!! 💥"
            else:
                # print(f"Already guessed ({row}, {col}). Try again!")
                return "Already guessed! Try again!"
        else:
            self.grid[row][col] = "❌" # Mark the miss
            # print(f"Miss at ({row}, {col})!")
            return "Miss! Better luck next time!"

    def all_ships_sunk(self):
        """
        This function checks if all ships have been sunk on this board.
        """

        return len(self.hits) == self.num_ships

def player_guess(board_size):
    """
    Ask player for coordinates and validates the input.
    """
    while True:
        try:
            guess_row = int(input(f"Guess a row (0-{board_size - 1}): \n"))
            guess_col = int(input(f"Guess a column (0-{board_size - 1}): \n"))
            if 0 <= guess_row < board_size and 0 <= guess_col < board_size:
                return (guess_row, guess_col)
            else:
                print(f"Invalid input. Please enter numbers between 0 and {board_size - 1}.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def cpu_guess(board_size, player_board_obj):
    """
    Generates a random guess for the CPU.
    """
    while True:
        guess_row = random.randint(0, board_size - 1)
        guess_col = random.randint(0, board_size - 1)
        if (guess_row, guess_col) not in player_board_obj.guesses_made:
            print(f"CPU guesses: ({guess_row}, {guess_col})")
            return (guess_row, guess_col)

def play_battleship():
    """
    Main function to play the Battleship game.
    """
    board_size = 5  # Size of the board
    num_ships = 5  # Number of ships
    player_board = Board(board_size, num_ships) # Create a player board
    cpu_board = Board(board_size, num_ships) # Create a CPU board

    player_board.place_ships()  # Place ships on the player's board
    cpu_board.place_ships()  # Place ships on the CPU's board

    print("Welcome to Battleship! 🎮")
    print(f"Hit the cpu's ships to win! You have {num_ships} ships to sink.")
    print(" '💥' = Hit '❌' = Miss ")

    turns = 0  # Initialize turns

    while not player_board.all_ships_sunk() and not cpu_board.all_ships_sunk():
        turns += 1
        print(f"\nTurn {turns}:")

        # Player's turn
        print("Your board (cpu guess here)")
        player_board.print_board()  # Print the player's board
        print("CPU's board (you guess here)")
        cpu_board.print_board()  # Print the CPU's board without showing
        print(f"Cpu has {num_ships - len(cpu_board.hits)} ships left to sink.")
        break



play_battleship()  # Start the game

# board = Board(5)
# board.place_ships()
# board.print_board()
# board.check_hit(2, 3)
# board.print_board()

# for row, col in board.ship_locations:
#     board.check_hit(row, col)
# print("All ships sunk?", board.all_ships_sunk())

# row, col = board.ship_locations[0]
# board.check_hit(row, col)
# board.check_hit(row, col)

# # player_guess(board.size)

# cpu_row, cpu_col = cpu_guess(board.size, board)
# print("CPU guessed:", cpu_row, cpu_col)

