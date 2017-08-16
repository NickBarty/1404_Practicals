def main():
    letter_frequency = frequency()
    name = get_name()
    print_name(name, letter_frequency)


def frequency():
    letter_frequency = int(input("Enter Letter Frequency: "))
    return letter_frequency


def print_name(name, letter_frequency):
    while len(name) < 1:
        name = input("Invalid, Please enter your name")
    if letter_frequency == 1:
        print(name[::letter_frequency])
    else:
        print(name[1::letter_frequency])


def get_name():
    name = input("Enter your name: ")
    return name


main()