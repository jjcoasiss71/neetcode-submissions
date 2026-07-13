class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        l, r = 0, 1
        res = 1
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                res = max(res, r - l)
            else:
                l, r = l + 1, l + 2
        return res