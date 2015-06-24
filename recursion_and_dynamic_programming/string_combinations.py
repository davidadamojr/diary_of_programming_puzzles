"""
Implement a function that prints all possible combinations of the characters 
in a string. These combinations range in length from one to the length of the 
string. Two combinations that differ only in ordering of their characters are 
the same combination. In other words, "12" and "31" are different combinations 
from the input string "123", but "21" is the same as "12".
"""
class Combinations:
    def __init__(self, input_string):
        # constructor 
        self.input_string = input_string
        self.comb_string = ""
        self.do_combinations(0)

    def do_combinations(self, start):
        i = start;
        while i < len(self.input_string):
            self.comb_string = self.comb_string + self.input_string[i]
            print self.comb_string
            self.do_combinations(i+1)
            self.comb_string = self.comb_string[:-1]
            i = i + 1

if __name__ == '__main__':
    combinations = Combinations("wxyz")


