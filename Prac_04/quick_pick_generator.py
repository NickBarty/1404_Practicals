import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("Enter how many quick picks to generate: "))
    while number_of_quick_picks < 0:
        print("Must be a number >0")
        number_of_quick_picks = int(input("Enter how many quick picks to generate: "))

    for i in range(number_of_quick_picks):
        numbers_list = []
        for x in range(NUMBERS_PER_LINE):
            generated_number = random.randint(MINIMUM, MAXIMUM)
            while generated_number in numbers_list:
                generated_number = random.randint(MINIMUM, MAXIMUM)
            numbers_list.append(generated_number)
        numbers_list.sort()
        print(" ".join("{:2}".format(generated_number) for generated_number in numbers_list))


main()
