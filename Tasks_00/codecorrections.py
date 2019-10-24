__author__ = "Oliver Theobald, 7146127"
# PART A
# current_time_str = input(,"What is the current time (in hours 0-23)?")
# Error 1: the datatype doesn't belong in the name 
# Error 2: the comma doesn't belong in the input brackets when you only have one part in there
current_time = input("What is the current time (in hours 0-23)? ")

# wait_time_str = input("How many hours do you want to wait"
# Error 1
# Error 3: Bracket missing at the end of the input statement
wait_time = input("How many hours do you want to wait? ")

# current_time_int = int(currentTimeStr)
# Error 1
# Error 4: value in int function isn't spelled right, so it's essentially not defined
current_time = int(current_time)

# wait_time_int = int(wait_time_str)
# Error 1
wait_time = int(wait_time)

# final_time_int = current_time_int + wait_time_int
# no errors
final_time = current_time + wait_time

# print(final_time_int)
# no errors
print("The time is now", final_time % 24)


# PART B
# no errors
# n = input("What time is it now (in hours)?")
n = input("What time is it now (in hours)?")

# n = imt(n)
# Error 5: spelling. The function is called int and not imt
n = int(n)

# m = input("How many hours do you want to wait?")
# no errors
m = input("How many hours do you want to wait?")

# m = int(m)
# no errors
m = int(m)

# prunt("The time is now", m % 12)
# Error 5
# Error 6: m % 12 doesn't make very much sense since it doesn't add the current time. It has to be (n+m) % 12
print("The time is now", (n+m) % 12)
