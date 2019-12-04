"""This module contains helper fuctions for the user interface."""



def input_number(prompt = "Please enter a number: "):
    """Read a number from the user."""
    
    while (True):
        try:
            number = int(input(prompt))
            return number
        except:
            print("You have to type a valid integer and press enter.")


def input_valid_number(prompt = "Please enter a vaild number: "):
    """Read a valid number from the user."""

    while (True):
        number = input_number(prompt)
        
        # Checks, wheather the number is in the valid range.
        if (11 <= number <= 66):
            return number
        else:
            print("A valid number is bigger than 10 and smaller than 67.")


def clear_screen(line_count):
    """Removes the current console text."""

    print("\n" * line_count)


def input_yes_no(prompt = "Write \"yes\" or \"no\": "):
    """Read only yes or no."""
    
    text = input(prompt)
    while (text != "yes" and text != "no"):
        text = input(prompt)

    return text


def print_points(player):
    """Print the points of the given player list."""

    print(player[0], "has (now) a total of", player[1], "points.")


