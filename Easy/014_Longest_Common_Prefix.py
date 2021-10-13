"""
LeetCode: 014_Longest_Common_Prefix.py
By Dongyoung Kim

참고:
https://www.youtube.com/watch?v=HVHv-iJfpp8&ab_channel=%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8

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