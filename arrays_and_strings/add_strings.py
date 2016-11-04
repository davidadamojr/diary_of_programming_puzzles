"""
Given two non-negative numbers "num1" and "num2" represented as string, return the sum of "num1" and "num2"

Note:
1. The length of both "num1" and "num2" is < 5100.
2. Both "num1" and "num2" contains only digits 0-9.
3. Both "num1" and "num2" does not contain any leading zero.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# @param num1 string
# @param num2 string
# @return result string

def add_strings(num1, num2):

    num1_idx = len(num1) - 1
    num2_idx = len(num2) - 1
    carry = 0

    result = ""

    while num1_idx >= 0 and num2_idx >=0:
        digit_sum = convert_to_int(num1[num1_idx]) + convert_to_int(num2[num2_idx]) + carry
        result_digit = digit_sum % 10
        carry = digit_sum / 10
        result = str(result_digit) + result

        num1_idx = num1_idx - 1
        num2_idx = num2_idx - 1

    while num1_idx >= 0:
        digit_sum = convert_to_int(num1[num1_idx]) + carry
        result_digit = digit_sum % 10
        carry = digit_sum / 10
        result = str(result_digit) + result

        num1_idx = num1_idx - 1

    while num2_idx >= 0:
        digit_sum = convert_to_int(num2[num2_idx]) + carry
        result_digit = digit_sum % 10
        carry = digit_sum / 10
        result = str(result_digit) + result

        num2_idx = num2_idx - 1

    if carry > 0:
        result = str(carry) + result

    return result


def convert_to_int(num):
    result = 0
    for digit_ch in num:
        digit_int = ord(digit_ch) - ord("0")
        result = result * 10 + digit_int

    return result

if __name__ == '__main__':
    assert add_strings("22", "22") == "44"
    assert add_strings("22", "2222") == "2244"
    assert add_strings("2222", "22") == "2244"
    assert add_strings("99", "99") == "198"
    assert add_strings("99", "999") == "1098"
    assert add_strings("999", "99") == "1098"
    print "All test cases passed successfully."


