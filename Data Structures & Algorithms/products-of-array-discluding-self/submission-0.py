class Solution:
    def prefixMul(self, nums, res, n):
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
            # 1 2 3 4
            n = len(nums)
            prefixRes = [1]*n # 1 1 1 1 -> 1 1 2 6
            self.prefixMul(nums, prefixRes, n)
            suffixRes = [1]*n
            self.prefixMul(nums[::-1], suffixRes, n)
            
            res = [0]*n
            for i in range(0, n):
                res[i] += prefixRes[i] * suffixRes[n-i-1]
            
            return res
            
            # 4 3 2 1
            # 1 1 1 1 -> 1 4 12 24 



        
        