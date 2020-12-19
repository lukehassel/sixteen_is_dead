__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import time

import entities.states.game_states as state
from entities.player.player_interface import PlayerInterface
from ui.ui_interface import UIInterface


class UIConsoleImpl(UIInterface):
    """
        This is the UI console Implementation. All methods are overridden from UIInterface.
    """

    def show_start_message(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Das Spiel hat gestartet.")
        print("Zum Beenden schreibe q. Um Neuzustarten Schreibe r")

    def show_current_player_move(self, player: PlayerInterface):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Spieler " + player.get_name() + " ist dran.")

    def restarting_game(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Das Spiel wird neu gestartet.")

    def show_did_not_roll(self, player: PlayerInterface):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Spieler " + player.get_name() + " hat nicht gewürfelt.")

    def show_dice_move_and_points(self, player: PlayerInterface, dice: [int]):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        for d in dice:
            print(player.get_name() + ": hat eine " + str(d) + " gewürfelt.")
        print(player.get_name() + " hat nun " + str(player.get_points()) + " Punkte.")

    def show_player_can_not_roll(self, player: PlayerInterface):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print(player.get_name() + ": darf nicht mehr würfeln. Akueller Punktestand: " + str(player.get_points()))

    def ask_player_to_RollState_dice_or_restart_game(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
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
            return self.ask_player_to_RollState_dice_or_restart_game()

    def show_player_has_to_roll_again(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Du musst nochmal würfeln. Nach 3 Sekunden warte Zeit geht es automatisch weiter.")
        time.sleep(3)

    def show_loser(self, player: PlayerInterface):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("------")
        print("Verloren hat: " + player.get_name())
        print("------")

    def show_same_points(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Verliere noch unklar: Es geht in die Nächste Runde.")

    def show_points_of_all_players(self, players: [PlayerInterface]):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        for player in players:
            print(player.get_name() + " hat " + str(player.get_points()) + " Punkte erreicht.")
