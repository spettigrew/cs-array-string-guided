"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. 
Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # Your code here

# U - Array has indices and does not contain negative numbers.
 #  - increments of 1, Only adding 1, so we need to only increment the last digit.
 # -  The array represents one whole number. 
 # If the number is 9, then index -1 to carry over the 1. last element and propogate forward.

 #Plan - 
    # Start at index of length of array
    #i = len(arr)
    # incrememt by one

    # if last digit is 9, then it needs to be 0 and carry over the one to the above index slot. 
    # Increment by one also (i - 1)
    # continue if previous digits are also 9
    # insert an index if first element is 9, add one as a new digit to the front.
    # add 1 to the last number if not a 9 and if 9 then make it a zero and repeat

    # index = len(digits) - 1         # index
    # while digits[index] == 9:       # while loop to check if index == 9
    #     digits[index] = 0           # check condition
    #     index = index - 1           # then decrement
    # if index == 1:                  # 
    #     digits.insert(0, 1)         
    # else: 
    #     digits[1] += 1

    # return digits

    # -----------------------------------------------------------------------------------------

    index = len(digits) - 1
    # loop until: until the current number is not 9 --> loop while the current number (digits[index]) is 9
    while index >= 0:
        # if the current number is 9:
        if digits[index] == 9:
            # set digits[index] = 0
            digits[index] = 0
            # repeat with the previous number
            index = index - 1
        # if it's not 9:
        else:
            # add 1 to digits[index]
            digits[index] += 1
            break
    # if we get to the beginning and it's 9 (index at 0): make it 10 (insert 1 at the beginning)
    if index == -1:
        digits.insert(0, 1)
    return digits




