def computer_to_phone(numbers):
    return numbers.translate(str.maketrans("123456789", "789456123"))
