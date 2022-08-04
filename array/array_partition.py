"""
LeetCode: 561. Array Partition [Easy]
By Dongyoung Kim

https://leetcode.com/problems/array-partition/

https://github.com/dkim4741
"""

# 1. Pythonic Way
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


# 2. Ascending Order
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # Calculate the sum by making pairs in ascending order from the front
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum


# 3. 짝수 번째 값 계산
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum
