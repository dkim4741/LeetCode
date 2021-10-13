"""
LeetCode: 001_Two_Sum.py
By Dongyoung Kim

https://github.com/dkim4741
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j];
                if sum == target:
                    return [i, j]
        
