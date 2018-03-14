rows = 4

for i in range(rows):
    print ' '*(rows-i-1) + '*'*(2*i+1)


"""Another solution could be:"""

rows = 4

for i in range(0,rows):
    spaces = rows - i - 1
    stars = i * 2 + 1
    print ' ' * spaces + '*' * stars