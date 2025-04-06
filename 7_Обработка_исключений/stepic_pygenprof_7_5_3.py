import sys

class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(password: str) -> PasswordError | bool:
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)
    checkLenPass = len(password) >= 9
    try:
        if not checkLenPass:
            raise LengthError
        elif not has_upper or not has_lower:
            raise LetterError
        elif not has_digit:
            raise DigitError
        return True
    except PasswordError as err :
        return err

pass_check = False
while not pass_check:
    password = input()
    pass_check_result = is_good_password(password)
    if pass_check_result == True:
        pass_check = True
        print('Success!')
    else:
        print(pass_check_result.__class__.__name__ )