COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
           "AntiqueWhite3": "#cdc0b0", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
           "azure1": "#f0ffff", "azure2": "#e0eeee", }

user_input = input("Enter a colour name: ")
while user_input != "":
    if user_input in COLOURS:
        print(COLOURS[user_input])
    else:
        print("Invalid colour name")
    user_input = input("Enter a colour name: ")