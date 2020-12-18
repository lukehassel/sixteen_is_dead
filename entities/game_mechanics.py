import sys

import entities.roll_dice as dice
import entities.states.game_states as states
import ui.ui_console_impl as ui
from entities.player.bot import Bot
from entities.player.player_interface import PlayerInterface
from entities.player.user import User
import random


class GameMechanics:

    def __init__(self, players: [PlayerInterface]):
        self.players = players

        tuple_list = []
        for i in players:
            tuple_list.append((i.getName(), isinstance(i, type(Bot(""))) and True or False))
        self.tuple = tuple_list
        self.sixteen_is_dead(tuple_list)

    DICE_COUNT = 3
    FACES_COUNT = 6
    SEED = 123
    state = states.GameInitialState()

    def sixteen_is_dead(self, players):
        """

        :param players: safsadf
        """
        ui.show_start_message()
        for player in self.players:
            if not (isinstance(self.state, type(states.RestartGame()))):
                self.player_move(player)
            else:
                pass
                # return None

        self.calculate_loser(self.players)
        ui.show_points_of_all_players(self.players)

    def player_move(self, player: PlayerInterface):
        """

        :param player:
        """
        ui.show_current_player_move(player)

        if isinstance(player, type(User(""))):
            self.user_move(player)
        elif isinstance(player, (type(Bot("")))):
            self.bot_move(player)

    def user_move(self, user: PlayerInterface):
        state = ui.ask_player_to_roll_dice_or_restart_game()
        self.state = state
        if isinstance(state, type(states.Roll())):
            self.roll(user)
            if self.can_roll(user):
                self.user_move(user)
            else:
                ui.showPlayerCanNotRoll(user)
        elif isinstance(state, type(states.NextPlayer())):
            pass
        elif isinstance(state, type(states.RestartGame())):
            self.restart()
        elif isinstance(state, type(states.EndGame())):
            sys.exit("Spiel wurde beendet.")

    def bot_move(self, bot: PlayerInterface):
        numberOfRolls = random.randint(0, 4)
        if numberOfRolls > 0:
            for i in range(0, numberOfRolls):
                self.roll(bot)
        else:
            ui.show_did_not_roll(bot)

    def calculate_loser(self, players: [PlayerInterface]):
        loser = min(players, key=lambda x: x.getPoints())
        if self.is_only_loser(players, loser.getPoints()):
            ui.show_loser(loser)
        else:
            ui.show_same_points()
            self.sixteen_is_dead(self.tuple)

    def roll(self, player: PlayerInterface):
        points = dice.roll_dice(self.DICE_COUNT, self.FACES_COUNT, self.SEED)
        player.addPoints(sum(points))
        ui.show_dice_move_and_points(player, points)
        if self.has_more_than_sixteen(player):
            ui.show_loser(player)
            ui.show_points_of_all_players(self.players)
            sys.exit()
        if self.has_to_roll_again(player):
            if isinstance(player, type(User(""))):
                ui.show_player_has_to_roll_again()
            self.roll(player)

    def is_only_loser(self, players: [PlayerInterface], points: int):
        list = []
        for p in players:
            if p.getPoints() == points:
                list.append(p)
        if len(list) == 1:
            return True
        else:
            return False

    def can_roll(self, player: PlayerInterface):
        return player.getPoints() != 9

    def has_to_roll_again(self, player: PlayerInterface):
        return player.getPoints() == 10

    def has_more_than_sixteen(self, player: PlayerInterface):
        return player.getPoints() > 15

    def restart(self):
        ui.restarting_game()
        for player in self.players:
            player.resetPoints()
        self.state = states.GameInitialState()
        self.sixteen_is_dead(self.tuple)
