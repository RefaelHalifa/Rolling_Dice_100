from utils import *
from game import *



def main():
    """Main Function in charge with the flow of the program"""
    print("Welcome to Dice Game!")
    player_1 = get_players_names(1)
    player_2 = get_players_names(2)
    total_score_1 = 0
    total_score_2 = 0
    current_choise_1 = "r"
    current_choise_2 = "r"
    while True:
        current_choise_1 = roll_menu(player_1, total_score_1)
        if check_double_pass(current_choise_1, current_choise_2):
            print("\n* We have found two passes *"
                  "\nCheking closer to 100!!")
            two_pass_menu(player_1, player_2, total_score_1, total_score_2)
            break
        if  current_choise_1:
            roll_1 = roll_dice()
            if check_over_100(sum_current(roll_1[2], total_score_1)):
                total_win_over_100(player_1, total_score_1, roll_1[2])
                break
            total_score_1 = sum_current(roll_1[2], total_score_1)
            print(f"\n{player_1} rolled {roll_1[0]} and {roll_1[1]} for a total of {roll_1[2]}"
                  f"\nCurrent Score Is {total_score_1}")

        current_choise_2 = roll_menu(player_2, total_score_2)
        if check_double_pass(current_choise_2, current_choise_1):
            print("\n* We have found two passes *"
                  "\nCheking closer to 100!!")
            two_pass_menu(player_1, player_2, total_score_1, total_score_2)
            break
        if  current_choise_2:
            roll_2 = roll_dice()
            if check_over_100(sum_current(roll_2[2], total_score_2)):
                total_win_over_100(player_2, total_score_2, roll_2[2])
                break
            total_score_2 = sum_current(roll_2[2], total_score_2)
            print(f"\n{player_2} rolled {roll_2[0]} and {roll_2[1]} for a total of {roll_2[2]}"
                  f"\nCurrent Score Is {total_score_2}")

    print("\nThanks for playing!")


main()


