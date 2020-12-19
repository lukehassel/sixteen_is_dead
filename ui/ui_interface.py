__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from abc import ABC, abstractmethod

from entities.player.player_interface import PlayerInterface


class UIInterface(ABC):
    @abstractmethod
    def show_start_message(self):
        """
            A method which shows the start Message and informations on how to quit and restart the game.
        """
        pass

    @abstractmethod
    def show_current_player_move(self, player: PlayerInterface):
        """
            A method which shows that the current player has to make his move.
            Args:
                player: This represents a bot class or a user class.
                        For more information on that take a look at the the bot  or user class.
        """
        pass

    @abstractmethod
    def restarting_game(self):
        """
            A method which shows that the the game is going to restart.
        """
        pass

    @abstractmethod
    def show_did_not_roll(self, player: PlayerInterface):
        """
            A method which shows that a player skipped his move.
            Args:
                player: This represents a bot class or a user class.
                        For more information on that take a look at the the bot  or user class.
        """
        pass

    @abstractmethod
    def show_dice_move_and_points(self, player: PlayerInterface, dice: [int]):
        """
            A method which shows the dice roll and how much points the player has after the dice roll.
            Args:
                player: This represents a bot class or a user class.
                        For more information on that take a look at the the bot  or user class.
                dice: A list of the thrown dices.
        """
        pass

    @abstractmethod
    def show_player_can_not_roll(self, player: PlayerInterface):
        """
            A method which shows that the player can not roll any more. It also prints the current points of the player.
            Args:
                player: This represents a bot class or a user class.
                        For more information on that take a look at the the bot  or user class.
        """
        pass

    @abstractmethod
    def ask_player_to_RollState_dice_or_restart_game(self):
        """
            A method which asks the user what to do next.
            The user can roll, quit, restart or can end his move.
            Returns:
                The corresponding game state from the user input as an instance of the GameState.
                For more informations take a look the the GameState class.
        """
        pass

    @abstractmethod
    def show_player_has_to_roll_again(self):
        """
            A method which shows that the player has to roll again. It waits for 3 seconds and then make the next roll
            automatically.
        """
        pass

    @abstractmethod
    def show_loser(self, player: PlayerInterface):
        """
            A method which shows which player has lost.
            Args:
                player: This represents a bot class or a user class.
                        For more information on that take a look at the the bot  or user class.
        """
        pass

    @abstractmethod
    def show_same_points(self):
        """
            A method which shows that there are multiple losers and that the game goes into the next round.
        """
        pass

    @abstractmethod
    def show_points_of_all_players(self, players: [PlayerInterface]):
        """
            A method which shows the points of all players.
            Args:
                players: List of all players. For more information on that take a look at the the PlayerInterface Interface.
        """
        pass
