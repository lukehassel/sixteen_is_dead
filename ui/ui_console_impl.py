import time

import entities.states.game_states as state
from entities.player.player_interface import PlayerInterface


def show_start_message():

    print("Das Spiel hat gestartet.")
    print("Zum Beenden schreibe q. Um Neuzustarten Schreibe r")


def show_current_player_move(player: PlayerInterface):
    print("Spieler " + player.getName() + " ist dran.")


def restarting_game():
    print("Das Spiel wird neu gestartet.")


def show_did_not_roll(player: PlayerInterface):
    print("Spieler " + player.getName() + " hat nicht gewürfelt.")


def show_dice_move_and_points(player: PlayerInterface, dice: [int]):
    for d in dice:
        print(player.getName() + ": hat eine " + str(d) + " gewürfelt.")
    print(player.getName() + " hat nun " + str(player.getPoints()) + " Punkte.")


def showPlayerCanNotRoll(player: PlayerInterface):
    print(player.getName() + ": darf nicht mehr würfeln. Akueller Punktestand: " + str(player.getPoints()))


# todo c)
# todo Returns True if the Player wants to roll the dice again. False if not.
def ask_player_to_roll_dice_or_restart_game():
    print("Zum würfeln drücke ENTER. Wenn du nicht mehr würfeln willst drücke n.")
    option = input("Deine Eingabe:")
    if option == "n":
        return state.NextPlayer()
    elif option == "":
        return state.Roll()
    elif option == "q":
        return state.EndGame()
    elif option == "r":
        return state.RestartGame()
    else:
        return ask_player_to_roll_dice_or_restart_game()


def show_player_has_to_roll_again():
    print("Du musst nochmal würfeln. Nach 3 Sekunden warte Zeit geht es automatisch weiter.")
    time.sleep(3)


def show_loser(player: PlayerInterface):
    print("------")
    print("Verloren hat: " + player.getName())
    print("------")


def show_same_points():
    print("Verliere noch unklar: Es geht in die Nächste Runde.")


def show_points_of_all_players(players: [PlayerInterface]):
    for player in players:
        print(player.getName() + " hat " + str(player.getPoints()) + " Punkte erreicht.")
