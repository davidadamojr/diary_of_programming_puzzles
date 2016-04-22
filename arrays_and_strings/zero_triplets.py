"""
Given an array of integers, return all triplets that sum up to zero.

For example, 

L = [-3, 2, -5, 8, -9, -2, 0, 1]
e = {-3, 2, 1}
Find all such e in L
"""

def naive_find_triplets(lst):
    # Naive solution: O(n^3)
    
    if not lst or len(lst) < 3:
        print None
        
    for i in range(0, len(lst)-2):
        for j in range(i, len(lst)-1):
            for k in range(j, len(lst)):
                triplet = [lst[i], lst[j], lst[k]]
                if sum(triplet) == 0:
                    print triplet

def find_triplets_with_hash_table(lst):
    """
    This solution uses a hash table to cut the time complexity down by n.
    Time complexity: O(n^2) instead of O(n^3) in the naive solution
    Space complexity: O(n)
    
    Hint: a+b+c = 0 => c = -(a+b)
    Once we know the first two elements of the triplet, we can compute the third 
    and check its existence in a hash table. In order to only get unique triplets, 
    we first sort the array, and mark off elements in the hash table
    """
    if not lst or len(lst) < 3:
        print None
        
    numbers = {}
    for number in lst:
        numbers[number] = False 
    
    for i in range(0, len(lst)-2):
        for j in range(i, len(lst)-1):
            first = lst[i]
            second = lst[j]
            third = -lst[i] - lst[j]
            if third in numbers and not numbers[third]:
                numbers[first] = True
                numbers[second] = True
                print [first, second, third]

def find_triplets(lst):
    """
    This solution achieves O(n^2) time complexity with no extra space requirements
    """
    
    if not lst or len(lst) < 3:
        print None
    
    # sort the list
    lst.sort()
    
    third_idx = len(lst) - 1
    first_idx = 0
    second_idx = first_idx + 1
    
    while third_idx > second_idx:
        sum = lst[first_idx] + lst[second_idx] + lst[third_idx]
        if sum > 0:
            third_idx = third_idx - 1
        elif sum < 0:
            second_idx = second_idx + 1
        else:
            print [lst[first_idx], lst[second_idx], lst[third_idx]]
            first_idx = first_idx + 1
            second_idx = first_idx + 1
    
    
    

if __name__ == "__main__":
    naive_find_triplets([-3,2,-5,8,-9,-2,0,1])
    print "======================"
    find_triplets_with_hash_table([-3,2,-5,8,-9,-2,0,1])
    print "======================"
    find_triplets([-3,2,-5,8,-9,-2,0,1])

