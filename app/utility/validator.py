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
    is_length_not_equal_13 = len(id) < 13 or len(id) > 13
    is_empty_string = id == ""
    is_not_digit = not id.isdigit()

    if is_length_not_equal_13 or is_empty_string or is_not_digit:
        return False

    return True


def validate_phone_number(phone_number):
    return True
