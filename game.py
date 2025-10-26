from utils import check_closer_100, roll_dice




def get_players_names(player: int) -> str:
    """Getting the player name"""
    return input(f"\nPlease enter player {player} name: ")


def validating_choice_roll(choice: str) -> bool:
    """Validating good input from the user"""
    if choice == "r" or choice == "p":
        return True
    else:
        return False


def roll_menu(player: str, current: int) -> bool:
    """the menu that each player gets when it's his turn"""
    choice = input(f"\n{player}'s turn:"
                   f"\nYour current score is {current}!"
                   f"\nPlease choose to Rooll or Pass"
                   f"\n* press 'r' to roll or 'p' to pass *"
                   f"\n -> ")
    while not validating_choice_roll(choice):
        choice = input("\nPlease enter a valid choice"
                       "\n* press 'r' to roll or 'p' to pass *"
                       "\n -> ")
    if choice == "r":
        return True
    else:
        return False


def total_win_over_100(player: str, current: int, current_roll: int) -> None:
    """the prompt a player gets when he wins do to score above 100"""
    print(f"\n{player} has passed 100!"
          f"\n{player} had {current} and rolled {current_roll}"
          f"\nfor a total of {current + current_roll}"
          f"\nCongratulations!!!")


def rotation_two_pass_roll(player_1: str, player_2: str) -> None:
    """the rolling the dice rotation after we noticed two passes"""
    while True:
        print(f"\nRolling {player_1}")
        roll_1 = roll_dice()
        print(f"You got {roll_1[0]} and {roll_1[1]} for a total of {roll_1[2]}")
        print(f"\nRolling {player_2}")
        roll_2 = roll_dice()
        print(f"You got {roll_2[0]} and {roll_2[1]} for a total of {roll_2[2]}")
        if roll_1[2] > roll_2[2]:
            print(f"\n{player_1} got bigger score so he is the winner!!")
            return
        elif roll_1[2] < roll_2[2]:
            print(f"\n{player_2} got bigger score so he is the winner!!")
            return


def two_pass_menu(player_1: str, player_2: str, current_1: int, current_2: int) -> None:
    """the prompt flow when we noticed two passes"""
    check_closer = check_closer_100(current_1, current_2)
    if check_closer == "Player_1":
        print(f"\n{player_1} is the closer to 100!"
              f"\nCongratulations!!!")
        return
    if check_closer == "Player_2":
        print(f"\n{player_2} is the closer to 100!"
              f"\nCongratulations!!!")
        return
    else:
        print("\nYou were Draw on closer to 100!"
              "\nBeginning rolling rounds: ")
        rotation_two_pass_roll(player_1, player_2)
        return

















