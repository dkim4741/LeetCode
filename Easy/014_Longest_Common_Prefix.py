"""
LeetCode: 014_Longest_Common_Prefix.py
By Dongyoung Kim

참고:
https://youtu.be/HVHv-iJfpp8

https://github.com/dkim4741
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        if not strs:
            return ""
        for i, ch in enumerate(strs(0)):
            for string in strs[i:]:
                if len(string) <= i or ch != string[i]:
                    return ''.join(ans)
            ans.append(ch)

        return ''.join(ans)
