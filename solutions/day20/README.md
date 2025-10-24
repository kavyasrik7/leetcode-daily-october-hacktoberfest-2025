Python solution
Problem: Final Value After Operations

Description:
You are given a list of strings operations, where each string represents an operation performed on a variable X (initially 0):

"++X" or "X++" → increment X by 1

"--X" or "X--" → decrement X by 1

Return the final value of X after performing all the operations.

My Approach:
I first initialized a counter count=0 to represent X. Then I looped through each operation in the list:
If "-" is in the string → decrement count by 1
Otherwise → increment count by 1
After the loop, return count as the final value.

Complexity Analysis
Time Complexity: O(n) → Loop through each operation once
Space Complexity: O(1) → Only one variable count is used

C++ solution
Problem: Final Value After Operations

Description:There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

My Approach:
The approach works by iterating through each operation in the given list and updating a variable `x` based on whether the operation is an increment or a decrement. For every string, the code checks if it contains a minus sign (`'-'`)—if it does, `x` is decreased by 1; otherwise, it is increased by 1. After processing all the operations, the final value of `x` is returned. This solution runs in linear time **O(n)** and uses **O(n)** space to store the operations.

Complexity Analysis
Time Complexity: O(n) 
Space Complexity: O(1) 

Java Solution
Problem : Final Value After Operations 

Approach

We initialize a variable X = 0 and iterate through the operations array.
For each operation, if it contains "++", we increment X; otherwise, we decrement it.
Finally, we return the value of X after all operations are performed.

Time Complexity: O(n) — we traverse the array once.
Space Complexity: O(1) — only a single integer variable is used.