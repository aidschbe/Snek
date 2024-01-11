import random


class Board:
    """
    Creates a playing field of 8x8.

    Author: hemmer
    Date: 2023-03-23
    Version: 0.6
    """

    def __init__(self, snake):
        """
        Constructor, initialises Snake and places snake and apple on the board.

        :param snake: An object of class Snake.
        """
        self.snake = snake
        self.place_snake()
        self.place_apple()

    # create dictionary to use as board
    field = {
        "A": list(),
        "B": list(),
        "C": list(),
        "D": list(),
        "E": list(),
        "F": list(),
        "G": list(),
        "H": list()
    }

    # fill dict entries with spaces to create empty board
    for key, value in field.items():
        for i in range(8):
            value.append(" ")

    # key set as actual list (as .keys() does not provide generic list)
    keys = list(field.keys())

    # current score
    score = 0

    # current location of head
    current_row = "E"
    current_col = 4

    # append each now move, delete & clear in board if no apple
    snake_coordinates = [["E", 2], ["E", 3], ["E", 4]]

    def print_score(self):
        """
        Prints score based on number of eaten apples.
        """
        print("Your score: {}".format(self.score))

    def check_win(self):
        """
        Checks win condition by looking for empty spaces on the board.
        :return: True if game is won, False if not.
        """
        for key, value in self.field.items():
            if " " in value:
                return False

            for i, j in self.field.items():
                if "O" in value:
                    return False
            print("Congratulations! You're now fat enough to fill your house. You win!")
            input("Press Enter to exit.")
            exit()

    def place_snake(self):
        """
        Sets snake in default position at the start of the game.
        """
        self.field.get(self.snake_coordinates[2][0])[self.snake_coordinates[2][1]] = self.snake.body[0]
        self.field.get(self.snake_coordinates[1][0])[self.snake_coordinates[1][1]] = self.snake.body[1]
        self.field.get(self.snake_coordinates[0][0])[self.snake_coordinates[0][1]] = self.snake.body[2]

    def set_row(self, new_row):
        """
        Sets new row for current location.
        Error and Game Over if outside borders of playing field.

        :param new_row: Given row of new location.
        """
        if new_row in range(len(self.keys)):
            self.current_row = self.keys[new_row]
        else:
            print("You crash headfirst into a wall and die. Wear your glasses next time. YOU LOSE!")
            self.print_score()
            input("Press Enter to exit")
            exit()

    def set_col(self, new_col):
        """
        Sets new column for current location.
        Error and Game Over if outside borders of playing field.

        :param new_col: Given column of new location.
        """
        if new_col in range(8):
            self.current_col = new_col
        else:
            print("You crash headfirst into a wall and die. Wear your glasses next time. YOU LOSE!")
            self.print_score()
            input("Press Enter exit")
            exit()

    def movement_mapping(self, direction):
        """
        Changes current location based on given movement input.

        :param direction: Given movement input in format WASD.
        """

        match direction:
            case "W":
                old_row = self.keys.index(self.current_row)
                new_row = old_row - 1
                self.set_row(new_row)

            case "A":
                new_col = self.current_col - 1
                self.set_col(new_col)

            case "S":
                old_row = self.keys.index(self.current_row)
                new_row = old_row + 1
                self.set_row(new_row)

            case "D":
                new_col = self.current_col + 1
                self.set_col(new_col)

    def move_head(self):
        """
        Move head of snake to new position.
        Append to snake location list.
        """
        self.field.get(self.current_row)[self.current_col] = self.snake.body[0]
        self.snake_coordinates.append([self.current_row, self.current_col])

    def move_tail(self):
        """
        Remove rearmost part of snake, so it doesn't grow with each move.
        Pops first (i.e. oldest) position in snake location list.
        """
        self.field.get(self.snake_coordinates[0][0])[self.snake_coordinates[0][1]] = " "
        self.snake_coordinates.pop(0)

    def move_snake(self, direction):
        """
        Moves snake across the board based on given direction.

        :param direction: Given new direction to move towards.
        """

        # align snake
        self.snake.change_direction(direction)
        self.field.get(self.current_row)[self.current_col] = self.snake.body[1]

        # convert input to new coordinates on board
        self.movement_mapping(direction)

        # if apple: increment score, move snake, place new random apple
        if self.field.get(self.current_row)[self.current_col] == "O":
            print("An apple a day and all that. Score + 1!")
            self.score += 1
            self.move_head()
            self.place_apple()

        # if self-cannibalism, game over
        elif self.field.get(self.current_row)[self.current_col] != " ":
            print("You try to imitate Ouroboros. You give yourself food poisoning. YOU LOSE!")
            self.print_score()
            input("Press Enter to exit.")
            exit()

        # if empty field, move snake, shorten snake
        else:
            self.move_head()
            self.move_tail()

    def place_apple(self):
        """
        Places apple on the board in a random, unoccupied space.
        """
        keys = list(self.field.keys())

        while True:
            random_row = random.choice(keys)
            random_column = random.choice(range(8))

            if self.field.get(random_row)[random_column] == " ":
                self.field.get(random_row)[random_column] = "O"
                break

    def print_board(self):
        """
        Prints current state of the board.
        """

        # print empty row
        print()

        # print column label
        print("#" * 35)
        print("## ~ ##  {}  {}  {}  {}  {}  {}  {}  {}  ##".format(1, 2, 3, 4, 5, 6, 7, 8))
        print("#" * 35)

        # print row label and board content
        for row in self.field:
            column = list(self.field.get(row))
            print("## {} ##  {}  {}  {}  {}  {}  {}  {}  {}  ##".format(
                row,
                column[0],
                column[1],
                column[2],
                column[3],
                column[4],
                column[5],
                column[6],
                column[7],
            ))

        print("#" * 35)
