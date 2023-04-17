def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2

def basic_op_refactored(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))
    
