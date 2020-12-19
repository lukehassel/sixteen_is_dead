__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"


class PlayerInterface:
    """
        This Class represents a player in the game.
    """

    def __init__(self, name: str):
        """
            A Constructor which initializes a player with the corresponding name.
            The points are here set to 0.
            Args:
                 name: The name of a player.
        """
        self.points = 0
        self.name = name

    def get_name(self):
        """
            A function to retrieve the name.
            :returns
                Name of the player.
        """
        return self.name

    def get_points(self):
        """
            A function to retrieve the points.
            :returns
                Points of the Player.
        """
        return self.points

    def add_points(self, points):
        """
            A function that adds a specific amount of points to the player.
            Args:
                 points: Number of points that should be added.
        """
        self.points = self.points + points

    def reset_points(self):
        """
            A function that resets the points to 0.
        """
        self.points = 0
