# Given a sorted array A of size n (with n at least 1) where A is uniquely filled with 
# integers in the range 1 to n + 1 such that there is one “missing integer” (the “missing 
# integer” is defined as the integer in the range 1 to n + 1 that is not in A), find that 
# “missing integer”. If the array only has one value, assume that the correct array with 
# no missing integer would be [1, 2]. If the array is empty or None, return 0. 

# You will be passed an object of type SpecialList. A SpecialList is a list that supports
# only two methods. You can call len on it to get the length of the SpecialList (i.e len(lst))
# You can also index it in O(1) time (i.e. lst[3]). Indexing is read-only however. 
# The size of SpecialList can be arbitrarily large

# Write Up
# s is the expected value at the start of the list and e is the expected value at the end of the list 
# s_idx is pointing to the start of the list and e_idx is pointing to the end of the list
# first check is to make sure the list is not empty, if it is return 0
# if list is not empty i check the value's at the opposite ends of the list 
# if those values are what they should be i increment and decrement the s_idx and e_idx respectively
# the expected values are also incremented and decremented accordingly for the next iteration
# if the expected value is not what it should be that value is returned and we are done
# the loop stops when the indexes meet

# Runtime:
# The loop stops when the index's meet in the middle of the array so the runtime is O(n/2)

# Space Complexity: O(n) for the lst of size n

from SpecialList import SpecialList

def find_missing_num(lst: 'SpecialList') -> int:
    if lst == None or lst == []:
        return 0 
        
    s = 1
    e = len(lst) + 1
    s_idx = 0
    e_idx = len(lst) -1
    if len(lst) == 0:
        return 0

    while s_idx <= e_idx:
        if lst[s_idx] != s:
            return s
        else:
            s_idx += 1
            s += 1
    
        if lst[e_idx] != e:
            return e
        else:
            e_idx -= 1
            e -= 1




    
