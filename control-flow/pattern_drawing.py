# pattern_drawing.py

# Ask the user for the size
size = int(input("Enter the size of the pattern: "))

# Validate positive input
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after a row is printed
        row += 1
