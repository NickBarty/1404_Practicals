LOWER = 33
UPPER = 127

letter = input("Enter a character: ")
while letter.isalpha() is False or len(letter) > 1:
    letter = input("Enter a character: ")
print("The ASCII code for {} is {}".format(letter, ord(letter)))
number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number < LOWER or number > UPPER:
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
print("The character for {} is {}".format(number, chr(number)))

for count in range(33, 127):
    print("{:<3} {}".format(count, chr(count)))
