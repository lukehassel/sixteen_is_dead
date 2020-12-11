class PlayerInterface:

    def __init__(self, name: str):
        self.points = 0
        self.name = name

    def getName(self):
        return self.name

    def getPoints(self):
        return self.points

    def addPoints(self, points):
        self.points = self.points + points

    def resetPoints(self):
        self.points = 0
