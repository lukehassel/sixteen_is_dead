import time

import entities.states.game_states as state
from entities.player.player_interface import PlayerInterface

"""
    This is the UI module. All Ui interactions are taking place here.
"""


def show_start_message():
    """
        A method which prints the start Message and informations on how to quit and restart the game.
    """
    print("Das Spiel hat gestartet.")
    print("Zum Beenden schreibe q. Um Neuzustarten Schreibe r")


def show_current_player_move(player: PlayerInterface):
    """
        A method which prints that the current player has to make his move.
        Args:
            player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
    """
    print("Spieler " + player.get_name() + " ist dran.")


def restarting_game():
    """
        A method which prints that the the game is going to restart.
    """
    print("Das Spiel wird neu gestartet.")


def show_did_not_roll(player: PlayerInterface):
    """
        A method which prints that a player skipped his move.
        Args:
            player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
    """
    print("Spieler " + player.get_name() + " hat nicht gewürfelt.")


def show_dice_move_and_points(player: PlayerInterface, dice: [int]):
    """
        A method which prints the dice roll and how much points the player has after the dice roll.
        Args:
            player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
    """
    for d in dice:
        print(player.get_name() + ": hat eine " + str(d) + " gewürfelt.")
    print(player.get_name() + " hat nun " + str(player.get_points()) + " Punkte.")


def show_player_can_not_roll(player: PlayerInterface):
    """
        A method which prints that the player can not roll any more. It also prints the current points of the player.
        Args:
            player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
    """
    print(player.get_name() + ": darf nicht mehr würfeln. Akueller Punktestand: " + str(player.get_points()))


# todo c)
# todo Returns True if the Player wants to RollState the dice again. False if not.
def ask_player_to_RollState_dice_or_restart_game():
    """
        A method which asks the user in the console what to do next.
        The user can roll, quit, restart or can end his move.
        Returns:
            The corresponding game state from the user input as an instance of the GameState.
            For more informations take a look the the GameState class.
    """
    print("Zum würfeln drücke ENTER. Wenn du nicht mehr würfeln willst drücke n.")
    option = input("Deine Eingabe:")
    if option == "n":
        return state.NextPlayerState()
    elif option == "":
        return state.RollState()
    elif option == "q":
        return state.EndGameState()
    elif option == "r":
        return state.RestartGameState()
    else:
        return ask_player_to_RollState_dice_or_restart_game()


def show_player_has_to_roll_again():
    """
        A method which prints that the player has to roll again. It waits for 3 seconds and then make the next roll
        automatically.
    """
    print("Du musst nochmal würfeln. Nach 3 Sekunden warte Zeit geht es automatisch weiter.")
    time.sleep(3)


def show_loser(player: PlayerInterface):
    """
        A method which prints which player hat lost.
        Args:
            player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
    """
    print("------")
    print("Verloren hat: " + player.get_name())
    print("------")


def show_same_points():
    """
        A method which prints that there are multiple losers and that the game goes into the next round.
    """
    print("Verliere noch unklar: Es geht in die Nächste Runde.")


def show_points_of_all_players(players: [PlayerInterface]):
    """
        A method which prints which player has lost.
        Args:
            players: List of all players. For more information on that take a look at the the PlayerInterface Interface.
    """
    for player in players:
        print(player.get_name() + " hat " + str(player.get_points()) + " Punkte erreicht.")
