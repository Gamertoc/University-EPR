__author__ = "Oliver Theobald, 7146127"

# This program checks whether an integer is happy or not. For this it squares every digit of the
# given integer and adds them to one vale. Rinse and repeat until a) the 1 is reached - the
# number is happy - or b) it ends in a periodic cycle of 4, 16, 37, 58, 89, 145, 42, 20,
# 4... - the number is unhappy.

n = input("Please enter a natural number: ")
save = n # We save the original number so we can use it in the output

count = 0 # This counts our iterations

while True:
    count += 1
    square = 0
    for i in range(len(n)):
        square += eval(n[i]) ** 2
    if square == 1:
        print(save, "is a happy number.")
        exit()
    elif square == 4:
        print(save, "is an unhappy number.")
        exit()
    elif count >= 100:
        print("Stopped after 100 iterations.")
        exit()

    n = str(square)
