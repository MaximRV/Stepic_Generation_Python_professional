def NumCount(n):
    count = 0
    def recurs(number):
        nonlocal count
        if number:
            count += 1
            if len(str(number)) == 1:
                return None
            else:
                recurs(int(str(number)[:-1]))

    recurs(n)
    return count
print(NumCount(int(input())))




test_number = 2
with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)

