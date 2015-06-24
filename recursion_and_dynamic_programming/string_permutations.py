"""
Implement a routine that prints all possible orderings of the characters in a 
string. In other words, print all permutations that use all the characters 
from the original string. For exaple, given the string "hat", your function should 
print the strings "tha", "aht", "tah", "ath", "hta", and "hat". Treat each 
character in the input string as a distinct character, even if it is repeated. 
Given the string "aaa", your routine should print "aaa" six times. You may print 
the permutations in any order you choose.
"""
class Permutation:
    def __init__(self, string):
        # create the boolean list/array that keeps track of whether a character 
        # has been used 
        self.used = {}
        for character in string:
            self.used[character] = False

        self.string = string
        self.permuted_string = ""

    def do_permutation(self):
        if len(self.permuted_string) == len(self.string):
            print self.permuted_string
            return
        else:
            for character in self.string:
                if self.used[character]:
                    continue
                self.permuted_string = self.permuted_string + character
                self.used[character] = True
                self.do_permutation()
                self.used[character] = False
                self.permuted_string = self.permuted_string[:len(self.permuted_string)-1]

if __name__ == "__main__":
    permutation = Permutation("abcd")
    permutation.do_permutation()






