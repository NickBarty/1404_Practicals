COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
           "AntiqueWhite3": "#cdc0b0", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
           "azure1": "#f0ffff", "azure2": "#e0eeee", }

user_input = input("Enter a colour name: ").strip()
while user_input != "":
    try:
        print("The code for {} is {}".format(user_input, COLOURS[user_input]))
        user_input = input("Enter a colour name: ")
    except KeyError:
        user_input = input("Invalid colour name! \nEnter a colour name: ").strip()
