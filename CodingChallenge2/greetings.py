# Greetings app

# Display one of 4 different greetings based on the time of day

# Good morning
# Good afternoon
# Good evening
# Good night

# For the time, use an integer from 0 - 23
# For example, 5-10 can represent "Good morning"

time = 12

if time >=5 and time < 10:
    print("Good morning")
elif time >=12 and time < 17:
    print("Good afternoon")
elif time >=17 and time < 22:
    print("Good evening")
else:
    print("Good night")