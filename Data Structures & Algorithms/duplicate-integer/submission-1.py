class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashedSet = set()
        for i in nums:
            if i in hashedSet:
                return True
            hashedSet.add(i)
        return False