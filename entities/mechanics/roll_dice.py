import random


def roll_dice(number=1, faces=6, seed=None):
    """
        A function which simulates the RollState of a dice.
        Args:
             number: Number of dices.
             faces: Faces of the dice.
             seed: To make this function return always the same random values when called.
        :returns
            Returns a list with Random values in the range of 1 to faces.
            The length of the list is defined by the Number of dices.
    """
    RollStates = []

    random.seed(seed)

    for r in range(0, number):
        RollStates.append(random.randint(1, faces))

    return RollStates
