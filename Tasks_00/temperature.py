__author__ = "Oliver Theobald, 7146127"
# We need to calculate the temperature in Fahrenheit based on a user input in 
# For this we need to a) get the user input, b) check if it's a number, c) check if it has a valid value,
# d) convert the value from Fahrenheit in Celsius, e) round it to a usable value and f) print the new value

# We start with the user input
temp_f = input(
    'Please enter the temperature in degree Fahrenheit (°F): ')

# Since we have to think of Lusers, it's necessary to check
# wether the input is in a correct form and a correct value
degree = False
value = False
while not value or not degree:
    degree = True
    value = True
    
    # I decided to use a try-except structure to test if the input value can be converted into an integer.
    # If this is the case, it continues to check wether it has a valid value (above absolute zero)
    # If it can't be converted (e.g. because it's a random string), it will throw an error that I catch in except
    # to keep the program running
    try:
        temp_f = eval(temp_f)
        if temp_f < -459.67:
            temp_f = input('Value too low! Such low temperatures do not exist.'
                                ' Please enter a valid temperature in degree Fahrenheit (°F): ')
            value = False

    # Getting a wrong input results in an error which we catch here and force the user to enter a valid value 
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

# Test values I used are:
# 1) random strings to test if it catches them and forces me to enter a number
# 2) values below the lowest possible temperature (like -1.000) to test the value catch
# 3) realistic values (32; 0; 100; 96) to test if the conversion works and to test the round function
