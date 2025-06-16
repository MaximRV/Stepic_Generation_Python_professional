def clock(numbersList):
    multiply_numbers = {1: 16, 2: 12, 3: 8, 4: 4}
    if numbersList:
        number = numbersList[0]
        multiplier = multiply_numbers[number]
        space = ' ' * ((16 - multiplier)//2)
        if multiplier == 4:
            print(f'{space}{str(number) * multiplier}{space}')
        else:
            print(f'{space}{str(number) * multiplier}{space}')
        del numbersList[0]
        clock(numbersList)

clock([1, 2, 3, 4, 3, 2, 1])
