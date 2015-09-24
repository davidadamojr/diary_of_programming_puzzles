"""
Write methods to implement the multiply, subtract and divide operations for 
integers. Use only the add operator.
"""

# In order to implement subtraction, we need to implement a negate function

# @param value integer value to be negated
# @return {Integer} negated value
def negate(value):
    # negates the value of its integer argument
    
    add_value = -1 if value > 0 else 1
    negated_value = 0
    
    while value != 0:
        negated_value = negated_value + add_value
        value = value + add_value
    
    return negated_value

def absolute(value):
    # returns the absolute value of its integer argument
    
    if value < 0:
        absolute_value = negate(value)
    else:
        absolute_value = value
    
    return absolute_value

# @param left_value first operand
# @param right_value second operand
# @return {Integer} result of subtracting right_value from left_value
def subtract(left_value, right_value):
    return left_value + negate(right_value)

# @param left_value first operand
# @param right_value second operand
# @return {Integer} result of multiplying left_value by right_value
def multiply(left_value, right_value):
    # a x b means add a to itself b times
    
    result = 0
    abs_right_value = absolute(right_value)
    for i in range(0, abs_right_value):
        result = result + left_value
    
    if right_value < 0:
        result = negate(result)
    
    return result

def divide(first_value, second_value):
    # x = a / b is the same as a = bx
    
    if second_value == 0:
        return "Error: division by zero"
    
    if first_value == 0:
        return 0
    
    result = 0
    mul_value = 0
    abs_first_value = absolute(first_value)
    abs_second_value = absolute(second_value)
    
    while mul_value < abs_first_value:
        mul_value = mul_value + abs_second_value
        if mul_value <= first_value:
            result = result + 1
    
    # the result is negative if the signs are different
    if first_value > 0 and second_value < 0:
        result = negate(result)
    elif first_value < 0 and second_value > 0:
        result = negate(result)
    
    return result

if __name__ == '__main__':
    # test negate function
    assert negate(5) == -5
    assert negate(-5) == 5
    assert negate(0) == 0
    
    # test absolute function
    assert absolute(5) == 5
    assert absolute(-5) == 5
    assert absolute(0) == 0
    
    # test subtraction
    assert subtract(5, -2) == 7
    print "5 - (-2) : " + str(subtract(5, -2))
    assert subtract(5, 2) == 3
    print "5 - 2 : " + str(subtract(5, 2))
    
    # test multiplication
    assert multiply(5, 0) == 0
    print "5 x 0 : " + str(multiply(5, 0))
    assert multiply(5, -2) == -10
    print "5 x -2 : " + str(multiply(5, -2))
    assert multiply(5, 2) == 10
    print "5 x 2 : " + str(multiply(5, 2))
    
    #test division
    assert divide(5, 0) == "Error: division by zero"
    print "5 / 0 : " + divide(5, 0)
    assert divide(0, 5) == 0
    print "0 / 5 : " + str(divide(0, 5))
    assert divide(5, -2) == -2
    print "5 / -2 : " + str(divide(5, -2))
    assert divide(10, 2) == 5
    print "10 / 2 : " + str(divide(10, 2))
    
    
    

