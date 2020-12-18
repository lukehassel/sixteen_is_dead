class GameState:
    """
        This class is the parent class of all the states in the game.
        For more information on the states take a look below.
    """
    pass


class GameInitialState(GameState):
    """
        This class represents a state in which the game can be.
        The GameInitialState is called at the beginning of the game.
    """
    pass


class NextPlayerState(GameState):
    """
        This class represents a state in which the game can be.
        The NextPlayerState is called when the user decides that the next player can throw the dice.
    """
    pass

class RollState(GameState):
    """
        This class represents a state in which the game can be.
        The RollState is called when the the user decides the roll the dice.
    """
    pass


class RestartGameState(GameState):
    """
        This class represents a state in which the game can be.
        The RestartGameState is called when the the user decides to restart the game.
    """
    pass


class EndGameState(GameState):
    """
        This class represents a state in which the game can be.
        The EndGameState is called when the the user decides to end the game.
    """
    pass
