#include <stdio.h>

# Matarr Cham 
# HW#2 CMSC389O
# 17 September 2021

# Write up
# Description: I started the (maxlen) variable at 1 because if the string is not an empty string then it has
# at least 1 character. I used a dictionary to store the data because i want to be able to efficently retrieve values
# With an array it would've decreased the performance because in order to obtain the values i need I would have to
# loop through the whole array multiple times.
# The first condition is to check if the string is empty. If it is, the longest substring (maxlen) is 0. 
# Otherwise I treat the string like an array and loop through the characters.
# If the character is not present in the dictionary, it is added to the dictionary and the value is the index 
# When the value has already been added to the hash. The index of the most recent occurence substracts the index
# of the last occurence (the stored value in the dictionary) to obtain the length. If the value obtained is greater 
# than the (maxlen) then that value is the new (maxlen). 
# Then the hash is updated, the value becomes the index of the recent occurence. At the end I return the maxlen

# Runtime: O(n) the algorithm only loops through the string once. 

# Space Complexity: At the most is O(n). The worst case is reached when every character is different, 
# the effect is every character must be stored in the dictionary. But if characters repeat they only need to be
# stored once with values being updated per occurence of the character. 
      
"""
Given a string, find the length of the longest substring without repeating characters.
*Note that the answer must be a substring (e.g. "abcd" is a subsequence of “abbbcccd”, not a substring).

Examples:
“abcabcbb” → 3 ("abc", with the length of 3)
“bbbbb” → 1 ("b", with the length of 1.)
“pwwkew” → 3 ("wke", with the length of 3)
"""

def longestString(s):
    maxlen = 1
    dict = {}

    if s == "":
        maxlen = 0
    else: 
        for (i,c) in enumerate(s):
            if dict.__contains__(c):
                if i-dict[c] >= maxlen:
                    maxlen = i - dict[c]
                    dict[c] = i
            else:
                dict[c] = i 
    return maxlen
