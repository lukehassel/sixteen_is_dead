__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from entities.mechanics.game_mechanics import GameMechanics
from entities.player.bot import Bot
from entities.player.user import User
from ui.factory.ui_console_factory import UIConsoleFactory

if __name__ == '__main__':
    """
        This method starts the program.
        It asks for the user for a name and initializes the ui.
        Then it will create a list of all the players.
        It will pass this as parameters to the GameMechanics class.
    """
    name = input("Gebe deinen Namen hier ein:")

    console_ui = UIConsoleFactory().initUI()

    players = [User(name), Bot("Bot1"), Bot("Bot2")]

    GameMechanics(players, console_ui)
