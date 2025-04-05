class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(password: str) -> bool:
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
        return type(err)

print(is_good_password('еПQSНгиfУЙ70qE'))