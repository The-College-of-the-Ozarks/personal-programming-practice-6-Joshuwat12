# remove.py


# Input
string = input("Enter a string: ")
char = input("Enter a single character: ")

# Incompatible bonus
# while len(char) != 1:
#   char = input("Please enter exactly one character: ")

# Computation
newString = ""
for letter in string:
  if not letter in char:
    newString += letter

# Output
print("When you remove everything in", char, "from", string + ", you get", newString)