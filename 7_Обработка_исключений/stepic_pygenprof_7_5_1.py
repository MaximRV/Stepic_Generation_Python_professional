
def is_good_password(password:str)->bool:
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)

    if all((has_upper,has_digit,has_lower,len(password) >= 9)):
        return True
    return False

print(is_good_password('МойПарольСамыйЛучший111'))

