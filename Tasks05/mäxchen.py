"""This is the main module and entry point of the game "Mäxchen"."""




import ui_help
import random as dice




def roll_dices():
    """Create a random valid number."""

    number_1 = dice.randint(1, 6)
    number_2 = dice.randint(1, 6)
    
    return max(number_1, number_2) * 10 + min(number_1, number_2)


def new_better_than_old(new_number, old_number):
    """Value two numbers.

    The number order is:
    42 > 21 > 66 > 55 > ... > 11 > others
    (others in the normal ">" order)

    """

    # Streching the numbers so we can easyly compare them.
    if new_number == 42:
        new_number *= 1000
    elif new_number == 21:
        new_number *= 100
    elif new_number % 10 == new_number // 10:
        new_number *= 10

    if old_number == 42:
        old_number *= 1000
    elif old_number == 21:
        old_number *= 100
    elif old_number % 10 == old_number // 10:
        old_number *= 10

    return new_number > old_number
    

def points_worth(number):
    """Calculate the points to subtract from the players account."""
    if (number == 42):
        return 3
    elif (number == 21):
        return 2

    return 1




def main():
    """The main entry point of the game."""

#             TEST
#         Remove later
#    for i in range(10):
#        n1 = roll_dices() #old
#        n2 = roll_dices() #new
#        print(n2, "better than", n1, "is", new_better_than_old(n2, n1))


    # +++++++++++INITIALIZE++++++++++++


    # Check the size of the user console.
    for i in range(150):
        print(150 - i)

    # The line_count is used to clear the screen.
    line_count = 2 + ui_help.input_number(\
        "What is the largest number you see without scrolling?: ")

    # Check, wheather the line count makes sense.
    if (line_count < 5):
        print("The game has not even started and you are already lieing...")
        return
    

    
    player_count = ui_help.input_number("How many players want to play? ")

    # Check, wheather the player count is valid. Is has to be 2 or larger
    if (player_count <= 0):
        print("Ok, you do not have to...")
        return
    elif (player_count == 1):
        print("Stop the jokes...")
        return
    else:
        print("Welcome to the game!")

    
    # The player list contains 2-elements-lists: [<name>, <points>].
    players = []
    
    for i in range(player_count):
        name = input("\nPlayer " + str(i + 1) + ": Please enter your name:\n")
        players.append([name, 10])
    


    # +++++++++GAME+++++++++++
    game_over = False
    last_diced_number = 0

    # This is the index of the player, who does the next move.
    # It is the list index, not the number.
    turn_index = 0
    
    while (not game_over):

        print("It is " + players[turn_index][0] + "'s turn.")

        diced_number = roll_dices()
        input("Press enter to show your number")
        print("You diced", diced_number)
        input("Press enter to hide your number")
        ui_help.clear_screen(line_count)

        print("The number from the last turn was", last_diced_number)

        typed_number = 0

        # This makes sure that a valid number is entered
        while (True):
            typed_number = ui_help.input_valid_number(\
                "Please enter the number you diced. (Its allowed to lie)")
    
            if (not new_better_than_old(typed_number, last_diced_number)):
                print("Of cause the number has to be bigger than the old one.")
                print("Read the rules and try again.")
            else:
                break

        next_turn_index = (turn_index + 1) % player_count
        
        believe = ui_help.input_yes_no(players[next_turn_index][0] + \
              " now decides. Do you believe it? Write \"yes\" or \"no\": ")

        # When not believing, check the numbers
        if (believe == "no"):
            print("Diced number:", diced_number, "Typed number:", typed_number)
            if (new_better_than_old(typed_number, diced_number)):
                print("Oops, you were caught red-handed.")
                print("Try to lie better next time ;)")
                players[turn_index][1] -= points_worth(typed_number)
                ui_help.print_points(players[turn_index])
            elif (typed_number == diced_number):
                print("No lie, no points for", players[next_turn_index][0])
                players[next_turn_index][1] -= points_worth(typed_number)
                ui_help.print_points(players[next_turn_index])
            else:
                print("It was a trap and you ran into it!")
                players[next_turn_index][1] -= points_worth(typed_number)
                ui_help.print_points(players[next_turn_index])

            #TO DO:
                #Update last_diced_number
                #Throw players with points <= 0 out of the game
                #Add a restart of the number after not believe and 42
                #End the game
                #etc...
                


        

        # Calculates the new player turn index.
        turn_index = (turn_index + 1) % player_count

        
    





# Starts the game, if run as main.
if __name__ == "__main__":
    main()
