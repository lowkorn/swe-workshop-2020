def validate_name(name):

    digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_char = ["!", "@", "#", "$"]
    space = " "

    if name == "":
        return False

    for char in name:
        is_digit = char in digit
        is_special_char = char in special_char
        is_space = char == space
        if is_digit or is_special_char or is_space:
            return False
    return True


def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
