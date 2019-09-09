"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# when a letter, symbol or nothing is received as an input

2. When will a ZeroDivisionError occur?
when the denominator (2nd number) is 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# yes, use a while loop to validate the denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Denominator cannot be 0, enter new denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
