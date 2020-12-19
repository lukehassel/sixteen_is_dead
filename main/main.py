from entities.mechanics.game_mechanics import GameMechanics
from entities.player.bot import Bot
from entities.player.user import User
from ui.factory.ui_console_factory import UIConsoleFactory

if __name__ == '__main__':

    name = input("Gebe deinen Namen hier ein:")

    console_ui = UIConsoleFactory().initUI()

    players = [User(name), Bot("Bot1"), Bot("Bot2")]

    GameMechanics(players, console_ui)
