__author__ = "Oliver Theobald, 7146127"
# We need to calculate the temperature in Fahrenheit based on a user input in Celsius
temp_f = input(
    'Please enter the temperature in degree Fahrenheit (°F): ')

# Since we have to think of Lusers, it's necessary to check
# wether the input is in a correct form and a correct value
degree = False
value = False
while not value or not degree:
    degree = True
    value = True
    try:
        temp_f = eval(temp_f)
        if temp_f < -459.67:
            temp_f = input('Value too low! Such low temperatures do not exist.'
                                ' Please enter a valid temperature in degree Fahrenheit (°F): ')
            value = False

    # Getting a wrong input results in an error which we catch here
    except (ValueError, NameError, SyntaxError) as e:
        print('Who the hell uses', temp_f, 'as temperature. What would that look like?\nHow cold is it today? '
                                               "-Oh, it's", temp_f, 'degree today.')
        temp_f = input(
            'Just enter the temperature in degree Fahrenheit (°F) as an integer or a float, okay? Here you go: ')
        degree = False

# Now that we have a correct form and value, the calculation can be done
temp_c = (temp_f-32) * 5 / 9

# Since we want to have a readable value we cut it down to two decimal places
temp_c = round(temp_c, 2)
if temp_c == int(temp_c):
    temp_c = int(temp_c)

print("The temperature ", temp_f, "°F equals ", temp_c, "°C.", sep = "")

# As test values I used valid integers and floats to verify the calculation itself,
# numbers that are too low to verify that it intercepts them as well as
# random strings to verify that it only accepts valid values.