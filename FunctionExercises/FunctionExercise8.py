# 8. Play again?

# Write a function that prompts the user for input, asking them "Do you want to play again (Y on N)?". If the user answers "Y", the function should return True, otherwise, it should return False.
reply = input("Do you want to play again (Y or N)? ")

def playAgain(x):
    if reply == "Y":
        return True
    else:
        return False