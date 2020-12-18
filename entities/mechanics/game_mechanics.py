import random
import sys

import entities.mechanics.roll_dice as dice
import entities.states.game_states as states
import ui.ui_console_impl as ui
from entities.player.bot import Bot
from entities.player.player_interface import PlayerInterface
from entities.player.user import User


class GameMechanics:

    def __init__(self, players: [PlayerInterface]):
        """
            Constructor which initializes the game.
            A tuple gets created from the players argument and is passed to the sixteen_is_dead method.
            Args:
                 players: This argument contains a list of the PlayerInterface.
                    For more information take a look at the PlayerInterface.
        """
        self.players = players

        tuple_list = []
        for i in players:
            tuple_list.append((i.get_name(), isinstance(i, type(Bot(""))) and True or False))
        self.tuple = tuple_list
        self.sixteen_is_dead(tuple_list)

    DICE_COUNT = 3
    FACES_COUNT = 6
    SEED = 123
    state = states.GameInitialState()

    def sixteen_is_dead(self, players):
        """
        This method starts the game. It shows in the ui that the game has started.
        It iterates the list a list of the PlayerInterface and calls for each player the player_move method.
        After that it calculates the loser and prints the loser in the console.
        Args:
            players: A tuple list which contains the Name and a boolean which is true when the player is a bot.
        """
        ui.show_start_message()
        for player in self.players:
            if not (isinstance(self.state, type(states.RestartGameState()))):
                self.player_move(player)
            else:
                pass
                # return None

        self.calculate_loser(self.players)
        ui.show_points_of_all_players(self.players)

    def player_move(self, player: PlayerInterface):
        """
        A method which calls the user_move method if the player object is a user.
        If not it calls the bot_move method.
        Args:
            players: A PlayerInterface which can represent a bot object or a user object.
                    For more information on that take a look at the bot class and the user class.
        """
        ui.show_current_player_move(player)

        if isinstance(player, type(User(""))):
            self.user_move(player)
        elif isinstance(player, (type(Bot("")))):
            self.bot_move(player)

    def user_move(self, user: PlayerInterface):
        """
            A method which asks the user in the console what he wants to do. For more information on that check out
            the method ask_player_to_RollState_dice_or_restart_game method in the ui_console_impl module.
            Depending on what the user choose for an input in the ask_player_to_RollState_dice_or_restart_game method
            the state of the game changes accordingly.
            Depending on the state this method then knows whether to restart the game, roll again or to end the game.
            Args:
                 user: Represents a user object.
                        For more information on that take a look at the the user class.
        """
        state = ui.ask_player_to_RollState_dice_or_restart_game()
        self.state = state
        if isinstance(state, type(states.RollState())):
            self.roll(user)
            if self.can_roll(user):
                self.user_move(user)
            else:
                ui.show_player_can_not_roll(user)
        elif isinstance(state, type(states.NextPlayerState())):
            pass
        elif isinstance(state, type(states.RestartGameState())):
            self.restart()
        elif isinstance(state, type(states.EndGameState())):
            sys.exit("Spiel wurde beendet.")

    def bot_move(self, bot: PlayerInterface):
        """
            A method which calculated how often the bot can roll the dice and then calls the roll method
            which then executes every sing roll.
            If the bot decided that he does not want to roll. It's printed in the console.
            Args:
                 bot: This represents a bot class. For more information on that take a look at the the bot class.
        """
        numberOfRollStates = random.randint(0, 4)
        if numberOfRollStates > 0:
            for i in range(0, numberOfRollStates):
                self.roll(bot)
        else:
            ui.show_did_not_roll(bot)

    def calculate_loser(self, players: [PlayerInterface]):
        """
            A method which calculates the loser. If there is more than one loser a new round will start.
            Args:
                 players: List of all players. For more information on that take a look at the the PlayerInterface Interface.
        """
        loser = min(players, key=lambda x: x.get_points())
        if self.is_only_loser(players, loser.get_points()):
            ui.show_loser(loser)
        else:
            ui.show_same_points()
            self.sixteen_is_dead(self.tuple)

    def roll(self, player: PlayerInterface):
        """
            A method which adds the point to the player object.
            This can be either a bot or a user.
            If the player hat more than sixteen it declares that player as the user and ends the game.
            If the player has to roll again this method is called again.
            Args:
                 player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
        """
        points = dice.roll_dice(self.DICE_COUNT, self.FACES_COUNT, self.SEED)
        player.add_points(sum(points))
        ui.show_dice_move_and_points(player, points)
        if self.has_sixteen(player):
            ui.show_loser(player)
            ui.show_points_of_all_players(self.players)
            sys.exit()
        if self.has_to_roll_again(player):
            if isinstance(player, type(User(""))):
                ui.show_player_has_to_roll_again()
            self.roll(player)

    def is_only_loser(self, players: [PlayerInterface], points: int):
        """
            It could be the case that in the end there are two or more players with the
            same points. If that's the case we don't have multiple losers.
            But we want only one loser.
            So this method checks if there is only one loser and returns True if there is.
            Else it's returning False.
            Args:
                 players: List of all players. For more information on that take a look at the the PlayerInterface Interface.
                 points: Integer of the points count of one loser.
            Returns:
                 True: If there is only one loser.
                 False: If there are multiple losers.
        """
        list = []
        for p in players:
            if p.get_points() == points:
                list.append(p)
        if len(list) == 1:
            return True
        else:
            return False

    def can_roll(self, player: PlayerInterface):
        """
            A method which checks if the player can roll the dice.
            Args:
                 player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
            Returns:
                 True: If the player can roll again.
                 False: If the player can't roll again.
        """
        return player.get_points() != 9

    def has_to_roll_again(self, player: PlayerInterface):
        """
            A method which checks if the player has to roll again.
            Args:
                 player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
            Returns:
                 True: If the player has to roll again.
                 False: If the player can't roll again.
        """
        return player.get_points() == 10

    def has_sixteen(self, player: PlayerInterface):
        """
            A method which checks if the player has more than 15 points.
            Args:
                 player: This represents a bot class or a user class.
                    For more information on that take a look at the the bot  or user class.
            Returns:
                 True: If the player has more than 15 points.
                 False: If the player does not have more than 15 points.
        """
        return player.get_points() > 15

    def restart(self):
        """
            This method restarts the game.
            It calls for every player the reset_points method. For more information on the reset_points method take a look
            at the PlayerInterface.
            The state of the game is set to the GameInitialState and the sixteen_is_dead method is called again.
        """
        ui.restarting_game()
        for player in self.players:
            player.reset_points()
        self.state = states.GameInitialState()
        self.sixteen_is_dead(self.tuple)
