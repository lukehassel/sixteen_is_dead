from entities.game_mechanics import GameMechanics
from entities.player.bot import Bot
from entities.player.user import User
from ui.ui_console_impl import ask_player_to_RollState_dice_or_restart_game
import ui.ui_console_impl as ui

if __name__ == '__main__':

    name = input("Gebe deinen Namen hier ein:")

    players = [User("name"), Bot("Bot1"), Bot("Bot2")]

    GameMechanics(players)
