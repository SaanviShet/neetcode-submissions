class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashedSet = []
        for i in range(0, len(nums)):
            hashedSet.append([i, nums[i]])
        sorted_items = sorted(hashedSet, key=lambda x: x[1])

        low = 0
        high = len(nums) - 1

        while(low <= high):
            if(sorted_items[low][1] + sorted_items[high][1] == target):
                return sorted([sorted_items[low][0], sorted_items[high][0]])
            elif(sorted_items[low][1] + sorted_items[high][1] > target):
                high -= 1
            else:
                low += 1
        