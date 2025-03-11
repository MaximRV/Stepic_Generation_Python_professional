import objgraph

my_list = [1, 2, 3]
objgraph.show_refs([my_list], filename='my_list.png')

#
#
# months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
#                6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
#                11: 'November', 12: 'December'}
# try:
#     number = int(input())
#     try:
#         print(months_dict[number])
#     except:
#         print('Введено число из недопустимого диапазона')
# except ValueError:
#     print('Введено некорректное значение')

