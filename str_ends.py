# str_ends.py


# Input
string = input("Enter a string: ")

# Computation
first = string[0]
last = string[-1]
midIndex = len(string) // 2

# Without this part, the middle characters for even-length strings would be wrong.
if len(string) % 2 == 0:
  midIndex -= 1
middle = string[midIndex]

# Output
print("The first character is", first)
print("The middle character is", middle)
print("The last character is", last)