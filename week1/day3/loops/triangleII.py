rows = int(raw_input("What is the height of the triangle? "))

for i in range(rows):
    print ' '*(rows-i-1) + '*'*(2*i+1)

