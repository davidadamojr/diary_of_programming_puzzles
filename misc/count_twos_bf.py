"""
Write a method to count the number of 2s between 0 and n
"""


# brute force solution
# sum up the number of twos in each digit from 0 to n

def number_of_twos(number):
    count = 0
    for i in range(2, number + 1):
        count = count + get_number_of_twos(i)

    return count


def get_number_of_twos(number):
    count = 0
    while number > 0:
        if number % 10 == 2:
            count = count + 1
        number = number / 10

    return count


if __name__ == '__main__':
    print(number_of_twos(100))
