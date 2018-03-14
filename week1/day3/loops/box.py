width = int(raw_input("What is the width of the box? "))
height = int(raw_input("What is the height of the box? "))

for row in range(height):
    if row == 0 or row == height - 1:
        print "*" * width
    else:
        spaces = width - 2
        print "*" + (" " * spaces) + "*"