import random


def roll_dice(number=1, faces=6, seed=None):
    """
        number = Anzahl an würfeln
        faces = Seiten des Würfels
        :returns
            Liste mit random werten von [1...faces].
            Die länge der liste ist definiert durch die Anzahl der Würfel
    """
    rolls = []

    random.seed(seed)

    for r in range(0, number):
        rolls.append(random.randint(1, faces))

    return rolls
