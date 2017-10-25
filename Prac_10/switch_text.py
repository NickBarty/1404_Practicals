file = 'switch.txt'
with open(file) as f:
    first_line = f.readline()

new_first_line = "in" if first_line == "out" else "out"

with open(file, 'w') as f:
    f.write(new_first_line)
