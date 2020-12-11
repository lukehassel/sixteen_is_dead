from entities.player.player_interface import PlayerInterface


class User(PlayerInterface):
    def __init__(self, name: str):
        super().__init__(name)

    def getName(self):
        return super().getName()

    def getPoints(self):
        return super().getPoints()

    def addPoints(self, points):
        super().addPoints(points)

    def resetPoints(self):
        super().resetPoints()
