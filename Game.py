"""
Snake ripoff.

Author: hemmer
Date: 2023-03-16
Version: 0.5
"""

from Board import Board
from Snake import Snake
from pynput import keyboard
import time
import os


class Game:
    """
    Game logic and input handling.

    Author: hemmer
    Date: 2023-03-16
    Version: 0.5
    """

    # initialise snake and game board
    snake = Snake()
    board = Board(snake)

    # default direction
    direction = "D"

    def on_press(self, key):
        """
        Necessary for pynput listener.
        Checks if key is a valid direction.
        If yes, changes global direction to key value.
        If no, passes, snake continues to move in previous direction.

        :param key: Key pressed down by user.
        """

        try:
            new_direction = key.char.upper()
            if new_direction in self.snake.directions:
                if self.snake.check_direction(new_direction):
                    self.direction = new_direction
        except AttributeError:
            pass

    def on_release(self, key):
        """
        Necessary for pynput listener.
        Empty since we only check key press, not key release.
        :param key: Key released by user after pressing.
        """
        pass

    def run(self):
        """
        Main function to run game.
        """

        # create listener to dynamically read user input.
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()

        self.board.print_board()

        input("Play with WASD. Press Enter to start.")

        while True:
            self.board.check_win()

            self.board.move_snake(self.direction)

            os.system('cls')

            self.board.print_board()

            time.sleep(1)


# create game and run it
snek = Game()
snek.run()
