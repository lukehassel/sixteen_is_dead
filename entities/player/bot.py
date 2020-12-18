from entities.player.player_interface import PlayerInterface


class Bot(PlayerInterface):

    """
        This class represents a computer as a player.
        All methods are overridden from the PlayerInterface class.
        For more information take a look at the PlayerInterface class.
    """

    def __init__(self, name: str):
        """
            This constructor is overridden by the PlayerInterface class.
            For more information take a look at the PlayerInterface class.
        """
        super().__init__(name)

    def get_name(self):
        """
            This method is overridden by the PlayerInterface class.
            For more information take a look at the PlayerInterface class.
        """
        return super().get_name()

    def get_points(self):
        """
            This method is overridden by the PlayerInterface class.
            For more information take a look at the PlayerInterface class.
        """
        return super().get_points()

    def add_points(self, points):
        """
            This method is overridden by the PlayerInterface class.
            For more information take a look at the PlayerInterface class.
        """
        super().add_points(points)

    def reset_points(self):
        """
            This method is overridden by the PlayerInterface class.
            For more information take a look at the PlayerInterface class.
        """
        super().reset_points()
