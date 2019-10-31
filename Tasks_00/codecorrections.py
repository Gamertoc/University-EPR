__author__ = "Oliver Theobald, 7146127"
# General rules:
# 1) The code has to be accepted by python
# 2) The code has to follow our conventions

# 3) In every instance where a variable is named the wrong way, I assume that by changing the
# original name all other instances of this variable are changed accordingly, and therefore
# won't write them up as errors.

# PART A
# current_time_str = input(,"What is the current time (in hours 0-23)?")
# Error 1: the data type doesn't belong in the name
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
# Error 1
final_time = current_time + wait_time

# print(final_time_int)
# Error 5: Without modulo 24 the function wouldn't make much sense
# since there can't be a time like 30 o' clock
print("The time is now", final_time % 24)


# PART B
# no errors
# n = input("What time is it now (in hours)?")
n = input("What time is it now (in hours)?")

# n = imt(n)
# Error 6: spelling. The function is called int and not imt
n = int(n)

# m = input("How many hours do you want to wait?")
# no errors
m = input("How many hours do you want to wait?")

# m = int(m)
# no errors
m = int(m)

# prunt("The time is now", m % 12)
# Error 6
# Error 7: m % 12 doesn't make very much sense since it doesn't add the current time.
# It has to be (n+m) % 12
print("The time is now", (n+m) % 12)
