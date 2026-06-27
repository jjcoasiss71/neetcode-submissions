class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = []
        for i in nums:
            if i not in appeared:
                appeared.append(i)
            else:
                return True
        return False