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
