# 9. Play again? Again.

# Write a function that asks the user whether they want to play again last the previous problem. Except this time, they have to answer with either "Y" or "N", if they give an invalid input, it should say "Invalid input." and prompt the user again for an answer. When the user finally gives a valid input, the function will return True if it was "Y", and False if it was "N".

reply = input("Do you want to play again (Y or N)? ")

def playAgain(x):
    if reply == "Y":
        print True
    if reply == "N":
        print False
    else:
        print("Invalid Input. Do you want to play again (Y or N)? ")
