columns = int(input("How many columns?:"))
rows = int(input("How many rows?:"))

for row in range(1,(rows + 1)):
    for col in range(1,(columns + 1)):
        length = len(str(col*row))
        space = ' ' * (4 - length)
        print(row*col , space , end = '')
    print('')
