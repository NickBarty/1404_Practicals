from Prac_07.car import Car

print("Lets drive!")
get_car_name = input("Enter your car name: ")
user_car = Car(get_car_name, 100)

print(user_car)
menu_selection = input("Menu: \nd) Drive \nr) Refuel \nq) Quit \nEnter your choice: ").upper()
while menu_selection != "Q":
    if menu_selection == "D":
        valid_input = False
        while not valid_input:
            try:
                distance_to_drive = int(input("How many km do you wish to drive? "))
                if distance_to_drive < 0:
                    print("Distance must be >= 0")
                    distance_to_drive = int(input("How many km do you wish to drive? "))
                else:
                    valid_input = True
            except ValueError:
                print("Invalid input")
        user_car.drive(distance_to_drive)
        print("The car drove {} km.\n".format(distance_to_drive))
    elif menu_selection == "R":
        valid_input = False
        while not valid_input:
            try:
                add_fuel = int(input("How many units of fuel do you want to add to the car? "))
                if add_fuel < 0:
                    print("Fuel amount must be >= 0")
                    add_fuel = int(input("How many units of fuel do you want to add to the car? "))
                else:
                    valid_input = True
            except ValueError:
                print("Invalid input")
        user_car.add_fuel(add_fuel)
        print("Added {} units of fuel\n".format(add_fuel))
    elif menu_selection == "":
        print("Menu input cannot be blank")
    else:
        print("Invalid menu choice \n")
    print(user_car)
    menu_selection = input("Menu: \nd) Drive \nr) Refuel \nq) Quit \nEnter your choice: ").upper()
print("Good bye {}'s driver.".format(user_car.name))