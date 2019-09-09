TARIFFS = {"11": 0.244618, "31": 0.136928, "23": 0.186996, "15": 0.435436, "29": 0.56387}

for key, value in TARIFFS.items():
    print("Tariff {} = ${}".format(key, value))
user_input = input("Enter a tariff to use: ")
while user_input != "":
    if user_input in TARIFFS:
        daily_use = float(input("Enter daily use in Kwh: "))
        billing_days = int(input("Enter number of billing days: "))
        total_cost = (billing_days * daily_use) * TARIFFS[user_input]
        print("Total cost is ${:.2f}".format(total_cost))
        user_input = input("Enter a tariff to use: ")
    else:
        user_input = input("Invalid tariff! \nEnter a valid tariff: ")
