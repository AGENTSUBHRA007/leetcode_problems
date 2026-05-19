class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        
        for k in range(n):
            d = nums[k]
            res_sum = 0  
            
            
            while d > 0:
                rem = d % 10
                res_sum = (res_sum * 10) + rem
                d = d // 10
            
            
            nums.append(res_sum)
            
        
        return len(set(nums))