"""
Implement an algorithm to print all valid (i.e., properly opened and closed) 
combinations of n-pairs of parentheses
"""

def all_valid_parentheses(num_pairs):
    """ Starting from the base case, insert a pair of parenthesis 
    into every pair from the combinations in the previous case """
    
    valid_parentheses = set([])

    def print_combinations(n, combinations):
        if n == 0:
            return valid_parentheses
        
        if n > num_pairs:
            return valid_parentheses
        
        new_combinations = set([])
        if n == 1:
            valid_parentheses.add("()")
            new_combinations.add("()")
        else:
            for combination in combinations:
                for i in range(0, len(combination)):
                    if combination[i] == '(':
                        inserted_str = insert_inside(combination, i)
                        valid_parentheses.add(inserted_str)
                        new_combinations.add(inserted_str)
                
                appended_combination = "()" + combination
                valid_parentheses.add(appended_combination)
                new_combinations.add(appended_combination)
    
        return print_combinations(n+1, new_combinations)
            
    # @param integer left the index of the left parenthesis of the currently considered pair
    # @param integer right the index of the right parenthesis of the currently considered pair
    def insert_inside(str, left):
        left_substr = str[0:left+1]
        right_substr = str[left+1:]
        inserted = left_substr + "()" + right_substr
        return inserted
    
    return print_combinations(1, set([]))
    
if __name__ == '__main__':
    assert all_valid_parentheses(1) == set(["()"])
    assert all_valid_parentheses(0) == set([])
    assert all_valid_parentheses(2) == set(["()", "(())", "()()"])
    print "All test cases passed."
        

