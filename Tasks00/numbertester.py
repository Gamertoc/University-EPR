__author__ = "7146127, Theobald"

number = input("Please enter an integer (maximum 5 digits): ")
testing = True
while testing:
    testing = False
    try:
        number = int(number)
        if number > 99999:
            number = input("Too large number! Try a smaller one: ")
            testing = True

    # Getting a wrong input results in an error which we catch here
    except (ValueError, NameError, SyntaxError) as e:
        number = input(
            'Wrong type! Please enter an integer with no more than 5 digits you stupid idiot: ')
        testing = True

# Separate thousands
thousands = number // 1000
digits = number % 1000
if digits < 10:
    digits = "00" + str(digits)
elif digits < 100:
    digits = "0" + str(digits)
    
if thousands > 0:
    print(thousands, ",", digits, sep="")
else:
    print(number)

# Check if it's an uneven number
if number % 2 == 1:
    print("The number is odd.")
else:
    print("The number is even.")


# Check if it's dividable by 7 with a rest of 3
if number % 7 == 3:
    print("You can divide the number by 7 and have a rest of 3.")
else:
    print("You can't divide the number by 7 and have a rest of 3.")
