import random
import sys

import entities.roll_dice as dice
import entities.states.game_states as states
import ui.ui_console_impl as ui
from entities.player.bot import Bot
from entities.player.player_interface import PlayerInterface
from entities.player.user import User


class GameMechanics:

    def __init__(self, players: [PlayerInterface]):
        self.players = players

        tuple_list = []
        for i in players:
            tuple_list.append((i.getName(), isinstance(i, type(Bot(""))) and True or False))
        self.sixteen_is_dead(tuple_list)

    DICE_COUNT = 3
    FACES_COUNT = 6
    SEED = 123
    state = states.GameInitialState()

    def sixteen_is_dead(self, players):
        ui.showStartMessage()

        for player in self.players:
            if not(isinstance(self.state, type(states.RestartGame()))):
                self.playerMove(player)
            else:
                pass
                #return None

        self.calculateLoser(self.players)
        ui.showPointsOfAllPlayers(self.players)

    def playerMove(self, player: PlayerInterface):
        ui.showCurrentPlayerMove(player)

        if isinstance(player, type(User(""))):
            self.userMove(player)
        elif isinstance(player, (type(Bot("")))):
            self.botMove(player)

    def userMove(self, user: PlayerInterface):
        state = ui.askPlayerToRollDiceOrRestartGame()
        self.state = state
        if isinstance(state, type(states.Roll())):
            self.roll(user)
            if self.canRoll(user):
                self.userMove(user)
            else:
                ui.showPlayerCanNotRoll(user)
        elif isinstance(state, type(states.NextPlayer())):
            pass
        elif isinstance(state, type(states.RestartGame())):
            self.restart()
        elif isinstance(state, type(states.EndGame())):
            sys.exit("Spiel wurde beendet.")

    def botMove(self, bot: PlayerInterface):
        numberOfRolls = random.randint(0, 4)
        if numberOfRolls > 0:
            for i in range(0, numberOfRolls):
                self.roll(bot)
        else:
            ui.showDidNotRoll(bot)

    def calculateLoser(self, players: [PlayerInterface]):
        loser = min(players, key=lambda x: x.getPoints())
        ui.showLoser(loser)

    def roll(self, player: PlayerInterface):
        points = dice.roll_dice(self.DICE_COUNT, self.FACES_COUNT, self.SEED)
        player.addPoints(sum(points))
        ui.showDiceMoveAndPoints(player, points)
        if self.hasMoreThanSixteen(player):
            ui.showLoser(player)
            ui.showPointsOfAllPlayers(self.players)
            sys.exit()
        if self.hasToRollAgain(player):
            self.roll(player)

    def canRoll(self, player: PlayerInterface):
        return player.getPoints() != 9

    def hasToRollAgain(self, player: PlayerInterface):
        return player.getPoints() == 10

    def hasMoreThanSixteen(self, player: PlayerInterface):
        return player.getPoints() > 15

    def restart(self):
        ui.restartingGame()
        for player in self.players:
            player.resetPoints()
        self.state = states.GameInitialState()
        self.sixteen_is_dead(None)

