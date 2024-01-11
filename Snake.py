class Snake:
    """
    Creates a snake object to represent the player

    Author: hemmer
    Date: 2023-03-15
    Version: 0.4
    """

    # variables for possible directions and corresponding snake renders.
    directions = ["W", "A", "S", "D"]
    head = ['^', '<', 'v', '>']
    body_parts = ['|', '—']

    # default snake when starting a game
    body = [head[3], body_parts[1], body_parts[1]]

    # default direction when starting game
    current_direction = "D"

    def opposite_direction(self):
        """
        Returns opposite of current direction, based on the self.directions list.

        :return: Returns opposite of given direction.
        """
        current_index = self.directions.index(self.current_direction)
        length = len(self.directions)
        if current_index < length / 2:
            return self.directions[current_index + 2]
        else:
            return self.directions[current_index - 2]

    def check_direction(self, direction):
        """
        Checks if direction allows for a valid move. Only invalid move is backwards.
        Prints error if invalid.

        :param direction: Given direction.
        :return: True if valid, False invalid.
        """
        if direction == self.opposite_direction():
            print("Error: Cannot move backwards.")
            return False
        return True

    def align_snake(self, new_head, new_body):
        """
        Aligns head and foremost body part.
        Parameters given by change_directon function.

        :param new_head: New head from head list.
        :param new_body: New body from body parts list.
        :return:
        """
        self.body[0] = new_head
        self.body[1] = new_body

    def change_direction(self, direction):
        """
        Changes front of snake based on given new direction.

        :param direction: Given direction in the format of WASD.

        :return: Return given direction if valid.
        """

        match direction:
            case "W":
                new_head = self.head[0]
                new_body = self.body_parts[0]

            case "A":
                new_head = self.head[1]
                new_body = self.body_parts[1]

            case "S":
                new_head = self.head[2]
                new_body = self.body_parts[0]

            case "D":
                new_head = self.head[3]
                new_body = self.body_parts[1]

        self.align_snake(new_head, new_body)  # align front of snake to new direction
        self.current_direction = direction  # update current direction of snake

        return direction
