def print_digits(number):
    if number:
        print(str(number)[:1])
        print_digits(str(number)[1:])

print_digits(12345)