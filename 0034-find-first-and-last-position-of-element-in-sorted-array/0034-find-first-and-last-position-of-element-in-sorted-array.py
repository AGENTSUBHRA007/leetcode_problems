class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = -1
        b = -1
        
        # Loop 1: Find the FIRST occurrence scanning Forward
        for i in range(len(nums)):
            if nums[i] == target:
                a = i
                break 
                
        # Loop 2: Find the LAST occurrence scanning Backward
        # Corrected range starts at the last index and ends at 0
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                b = j 
                break # Stop immediately since we are traveling backward!
                
        return [a, b]