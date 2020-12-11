import entities.states.game_states as state
from entities.player.player_interface import PlayerInterface


# todo a)
def showStartMessage():
    print("Das Spiel hat gestartet.")
    print("Zum Beenden schreibe q. Um Neuzustarten Schreibe r")


# todo b)
def showCurrentPlayerMove(player: PlayerInterface):
    print("Spieler " + player.getName() + " ist dran.")


def restartingGame():
    print("Das Spiel wird neu gestartet.")


def showDidNotRoll(player: PlayerInterface):
    print("Spieler " + player.getName() + " hat nicht gewürfelt.")


def showDiceMoveAndPoints(player: PlayerInterface, dice: [int]):
    for d in dice:
        print(player.getName()+": hat eine "+str(d)+" gewürfelt.")
    print(player.getName() + " hat nun " + str(player.getPoints()) + " Punkte.")


def showPlayerCanNotRoll(player: PlayerInterface):
    print(player.getName() + ": darf nicht mehr würfeln. Akueller Punktestand: " + str(player.getPoints()))


# todo c)
# todo Returns True if the Player wants to roll the dice again. False if not.
def askPlayerToRollDiceOrRestartGame():
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
        return askPlayerToRollDiceOrRestartGame()


def showLoser(player: PlayerInterface):
    print("------")
    print("Verloren hat: " + player.getName())
    print("------")


def showPointsOfAllPlayers(players: [PlayerInterface]):
    for player in players:
        print(player.getName() + " hat " + str(player.getPoints()) + " Punkte erreicht.")
