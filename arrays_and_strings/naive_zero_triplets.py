"""
Given an array of integers, return all triplets that sum up to zero.

For example, 

L = [-3, 2, -5, 8, -9, -2, 0, 1]
e = {-3, 2, 1}
Find all such e in L

Naive solution: O(n^3)
"""

def find_triplets(arr):
    for i in range(0, len(arr)-2):
        for j in range(i, len(arr)-1):
            for k in range(j, len(arr)):
                triplet = [arr[i], arr[j], arr[k]]
                if sum(triplet) == 0:
                    print triplet

if __name__ == "__main__":
    find_triplets([-3,2,-5,8,-9,-2,0,1])

