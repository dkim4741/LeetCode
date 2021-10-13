"""
LeetCode: 136_Single_Number.py
By Dongyoung Kim

https://github.com/dkim4741
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a