import sys

data = [int(line.strip()) for line in sys.stdin]

def reverseOrder(data):
    if data:
        if data[0] == 0:
            print(data[0])
        else:
            reverseOrder(data[1:])
            print(data[0])


reverseOrder(data)



test_number = 1
with open(f'/media/maxim/Data/projects/Stepic_Generation_Python_professional/tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'/media/maxim/Data/projects/Stepic_Generation_Python_professional/tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)