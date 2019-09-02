"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

# state = input("Enter short state: ").upper()
# while state != "":
# CHECK THIS FOR LOOP EXISTS!!!!!!!!!!!!!!!!
for state in STATE_NAMES:
    # if state in STATE_NAMES:
    print(f"{state.upper():3} is {STATE_NAMES[state]}")
# else:
#     print("Invalid short state")
# state = input("Enter short state: ").upper()
