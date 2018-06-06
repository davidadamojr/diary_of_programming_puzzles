"""
We are stacking blocks to form a pyramid. Each block has a color which 
is a one letter string like "Z". For every block of "C", we place not in 
the bottom row, we are placing it on top of a left block of color "A" and right
block of color "B". We are allowed to place the block there only if "(A,B,C)" is 
an allowed triple. 

We start with a bottom row of "bottom", represented as a single string. 
We also start with a list of allowed triples "allowed". Each allowed triple is 
represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
                A
               / \
              D   E
             / \ / \
            X   Y  Z
            
This works because ('X','Y','D'), ('Y','Z','E') and ('D','E','A') 
are allowed triples.

https://leetcode.com/problems/pyramid-transition-matrix
"""


def pyramid_transition_matrix(bottom, allowed):
    chars, allowed = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}, set(allowed)

    def dfs(row, q, i):
        if len(row) == 1:
            return True

        for c in chars:
            if row[i: i+2] + c in allowed:
                if i == len(row) - 2 and dfs(q + c, "", 0):
                    return True
                elif dfs(row, q + c, i + 1):
                    return True
        return False

    return dfs(bottom, "", 0)

assert pyramid_transition_matrix("ABC", ["ABD", "BCE", "DEF", "FFF"]) is True
print("All tests passed successfully.")
