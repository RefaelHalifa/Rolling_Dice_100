import random




def roll_dice() -> tuple:
    """Rolling The Dice"""
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1, dice_2, dice_1 + dice_2


def sum_current(dice: int, current: int) -> int:
    """Summary of the output from the dice with the current total"""
    return dice + current


def check_over_100(current: int) -> bool:
    """Checking The total score if it is over 100"""
    if current >= 100:
        return True
    else:
        return False


def check_closer_100(current_1: int, current_2: int) -> str:
    """Checking how's score is closer to 100"""
    if (100 - current_1) < (100 - current_2):
        return "Player_1"
    elif (100 - current_1) > (100 - current_2):
        return "Player_2"
    else:
        return "Draw"


def bigger_roll(palyer_1: int, palyer_2: int):
    """Checking the bigger roll"""
    if palyer_1 > palyer_2:
        return "Player_1"
    elif palyer_1 < palyer_2:
        return "Player_2"
    else:
        return "Draw"


def check_double_pass(choice_1: bool, choice_2: bool) -> bool:
    """Checking for a dubble pass, from the las choice and the one before"""
    if choice_1 == False and choice_2 == False:
        return True
    else:
        return False


