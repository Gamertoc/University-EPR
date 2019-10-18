__author__ = "Oliver Theobald, 7146127"

current_time = int(input("What is the current time (in hours 0-23)? "))
wait_time = int(input("How many hours do you want to wait? "))
final_time = current_time + wait_time
print("Waiting will end at", final_time % 24, "o' clock.")

n = int(input("What time is it now (in hours)? "))
m = int(input("How many hours do you want to wait? "))
print("The time is now", (n+m) % 24, "o' clock.")
