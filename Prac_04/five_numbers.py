numbers = []
counter = 1
number_to_append = (int(input("Number {}: ".format(counter))))
numbers.append(number_to_append)
counter += 1
while number_to_append >= 0:
    number_to_append = (int(input("Number {}: ".format(counter))))
    numbers.append(number_to_append)
    counter += 1
numbers.pop()
print("The first number is -------------{:>5}".format(numbers[0]))
print("The last number is --------------{:>5}".format(numbers[-1]))
print("The smallest number is ----------{:>5}".format(min(numbers)))
print("The largest number is -----------{:>5}".format(max(numbers)))
print("The average of the numbers is ---{:>7}".format(sum(numbers) / len(numbers)))
