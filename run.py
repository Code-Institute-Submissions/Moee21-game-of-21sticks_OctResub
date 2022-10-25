"""
got idea and inspiration from:
https://www.youtube.com/watch?v=ReQz7vwDjPs&ab_channel=NickyDylewski
https://www.youtube.com/watch?v=SdrSEq_dsBU&t=326s&ab_channel=3ATeam
"""

STICKS = 21          # Total number of match sticks

print("Welcome to 21 MatchSticks Game.\n")

print("This program is a game which you will play against the computer.")
print("You could only win if you are not left with last 1 stick.")
print("Please, enter One Number from 1-4 of sticks at each turn.")
print("So let us begin with the game! \n")

print("Total Sticks:", STICKS, "\n")

while STICKS > 1:  # Program will run till sticks are greater than 1
    user = int(input("User(1,2,3,4): "))   # User input int numbers from 1-4

    while user not in [1, 2, 3, 4]:
        print("Invalid input. Please try again.")
        user = int(input("User(1,2,3,4): \n"))

    user_turn = False  
    # setting user var to False means next turn is computer's
    STICKS -= user
    print("Sticks left: ", STICKS, "\n")

    computer = 5 - user   # Computer's choice
    print("Computer: ", computer)

    user_turn = True    # setting user var to True means next turn is user's
    STICKS -= computer
    print("Sticks left: ", STICKS, "\n")

if user_turn:  # if user_turn is True means next turn is user's
    print("User Lost")

else:       # If it is False means next turn is computer's
    print("Computer lost")  
    # This condition will never be triggered since computer will never lose.  
