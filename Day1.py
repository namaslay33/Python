# Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
# Output :
# Twinkle, twinkle, little star,
#     How I wonder what you are! 
#         Up above the world so high,
#         Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#     How I wonder what you are

print("Twinkle, twinkle, litte star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamon in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your name?")
age = input("How old are you?")

num = 100 - age
year100 = 2018 + num

print("Hello, " + name + ". You will turn 100 in " + str(year100) + ".")

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

n = int(input("Enter in a number: "))

n1 = int( "%s" % n )
n2 = int( "%s%s" % (n,n) )
n3 = int( "%s%s%s" % (n,n,n) )

print(n1 + n2 + n3)
