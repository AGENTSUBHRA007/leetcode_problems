class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count=1
        nums.sort()
        k=len(nums) - 1
        for i in range(k):
            if nums[i] == nums[i+1]:
                return nums[i] 
                
        return -1
    
                
        