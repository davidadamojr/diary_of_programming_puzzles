"""
Seive of Eratosthenes - Efficiently generate a list of primes
Non-prime numbers are divisible by prime numbers
0 and 1 are not prime numbers
"""
def initialize_list(max):
    boolean_list = []
    for i in xrange(0, max+1):
        if i == 0 or i == 1:
            boolean_list.append(False)
        else:
            boolean_list.append(True)

    return boolean_list

def cross_off(boolean_list, prime_number):
    """
    cross off multiples of "prime_number"
    """
    for i in xrange(prime_number*prime_number, len(boolean_list), prime_number):
        boolean_list[i] = False

def get_next_prime(boolean_list, prime_number):
    next_prime = prime_number + 1
    while next_prime < len(boolean_list) and not boolean_list[next_prime]:
        next_prime = next_prime + 1

    return next_prime

def seive_of_eratosthenes(max):
    boolean_list = initialize_list(max)
    prime_number = 2

    while prime_number < len(boolean_list):
        cross_off(boolean_list, prime_number)
        prime_number = get_next_prime(boolean_list, prime_number)

    # print prime numbers up to max
    for index in xrange(0, len(boolean_list)):
        if boolean_list[index]:
            print index,

seive_of_eratosthenes(40)
