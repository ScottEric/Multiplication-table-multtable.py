for row in range(1,13):
    for col in range(1,13):
        length = len(str(col*row))
        space = ' ' * (4 - length)
        print(row*col , space , end = '')
    print('')
