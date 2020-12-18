import time

import entities.states.game_states as state
from entities.player.player_interface import PlayerInterface


def show_start_message():
    print("Das Spiel hat gestartet.")
    print("Zum Beenden schreibe q. Um Neuzustarten Schreibe r")


def show_current_player_move(player: PlayerInterface):
    print("Spieler " + player.get_name() + " ist dran.")


def restarting_game():
    print("Das Spiel wird neu gestartet.")


def show_did_not_RollState(player: PlayerInterface):
    print("Spieler " + player.get_name() + " hat nicht gewürfelt.")


def show_dice_move_and_points(player: PlayerInterface, dice: [int]):
    for d in dice:
        print(player.get_name() + ": hat eine " + str(d) + " gewürfelt.")
    print(player.get_name() + " hat nun " + str(player.get_points()) + " Punkte.")


def showPlayerCanNotRollState(player: PlayerInterface):
    print(player.get_name() + ": darf nicht mehr würfeln. Akueller Punktestand: " + str(player.get_points()))


# todo c)
# todo Returns True if the Player wants to RollState the dice again. False if not.
def ask_player_to_RollState_dice_or_restart_game():
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
    print("Du musst nochmal würfeln. Nach 3 Sekunden warte Zeit geht es automatisch weiter.")
    time.sleep(3)


def show_loser(player: PlayerInterface):
    print("------")
    print("Verloren hat: " + player.get_name())
    print("------")


def show_same_points():
    print("Verliere noch unklar: Es geht in die Nächste Runde.")


def show_points_of_all_players(players: [PlayerInterface]):
    for player in players:
        print(player.get_name() + " hat " + str(player.get_points()) + " Punkte erreicht.")
