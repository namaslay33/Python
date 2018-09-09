#Loop Exercises

# #1 to 10
for number in range(1, 11):
    print(number)

# #2 n to m
n = int(input("What's the starting number?"))
m = int(input("what's the ending number?"))


for number in range(n, m):
    print(number)

# #3 Odd Number
odd = []
for number in range(1, 11):
    if number % 2 != 0 :
        odd.append(number)
        print(number)

#4 Print a Square
characters = ['***** ', '***** ', '***** ', '***** ', '***** ']
for character in characters:
    print(character)

# #5 Print a Square II
n = int(input("How big is the square?"))
character = "*"

for i in range(n):
    print(character * n)

#6 Print a Box

height = int(input("Height?"))
width = int(input("Width?"))

character = "*"
print(height * character)

numSpace = width - 2
spaces = ' ' * numSpace

for i in range(height - 2):
    print(character + spaces + character)

print(character * height)


# #7 Print a Triangle
character = "*"
height = 8


for h in range (height):
    print((character) * (h + 1))

# #8 Print a Triangle II
# (Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.)

character = "*"
height = int(input("Provide a height: "))


for j in range (height):
    print((character) * (j + 1))

# #9 Multiplication Table

for i in range(1,11):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print("------Next Section-----")