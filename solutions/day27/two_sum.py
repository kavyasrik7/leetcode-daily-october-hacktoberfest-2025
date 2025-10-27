"""
LeetCode Problem: 1. Two Sum
Difficulty: Easy
Date: October 27, 2025

Problem Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Author: [Alina]
GitHub: [Alina1902]
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Approach: Hash Map (Dictionary)
        
        Time Complexity: O(n) - We traverse the list once
        Space Complexity: O(n) - In worst case, we store all elements in hash map
        
        Algorithm:
        1. Create an empty hash map to store number and its index
        2. Iterate through the array
        3. For each element, calculate complement (target - current number)
        4. Check if complement exists in hash map
        5. If yes, return the indices
        6. If no, add current number and index to hash map
        """
        
        # Hash map to store number -> index mapping
        num_map = {}
        
        # Iterate through the array with index and value
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # Check if complement exists in our hash map
            if complement in num_map:
                # Found the pair! Return indices
                return [num_map[complement], i]
            
            # Store current number and its index in hash map
            num_map[num] = i
        
        # This line should never be reached given problem constraints
        return []


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: {solution.twoSum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2: {solution.twoSum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test 3: {solution.twoSum(nums3, target3)}")  # Expected: [0, 1]
    
    # Test Case 4 (Negative numbers)
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    print(f"Test 4: {solution.twoSum(nums4, target4)}")  # Expected: [2, 4]


"""
Alternative Approach - Brute Force (Not Recommended)

Time Complexity: O(n^2)
Space Complexity: O(1)

def twoSum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

This approach checks every pair but is inefficient for large inputs.
"""
