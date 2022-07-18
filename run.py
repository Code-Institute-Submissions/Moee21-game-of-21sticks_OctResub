"""
got idea and inspiration from:
https://www.youtube.com/watch?v=ReQz7vwDjPs&ab_channel=NickyDylewski
https://www.youtube.com/watch?v=SdrSEq_dsBU&t=326s&ab_channel=3ATeam
"""

STICKS = 21          # Total number of match sticks

print("This program is a game which you will play against the computer")
print("In this game there are 21 sticks and")
print("you have to pick up 1-4 number of sticks each turn ")
print("The way you win is by not taking the last stick \n")

print("Total Sticks:", STICKS, "\n")

while STICKS > 1:  # Program will run till sticks are greater than 1
    user = int(input("User(1,2,3,4): ")) # User input int numbers from 1-4

    user_turn = False  # setting user var to False means next turn is computer's
    STICKS -= user
    print("Sticks left: ", STICKS, "\n")

    computer = 5 - user   # Computer's choice
    print("Computer: ", computer)

    user_turn = True    #setting user var to True means next turn is user's
    STICKS -= computer
    print("Sticks left: ", STICKS, "\n")

    while user not in [1,2,3,4]:
        print("Invalid input. Please try again.")
        user = int(input("User(1,2,3,4): "))

