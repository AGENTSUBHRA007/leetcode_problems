class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                # FIX 1: Use square brackets for lists
                if target == nums[i] + nums[j]:
                    return [i, j]
                    
        # FIX 2: Only return -1 AFTER both loops are completely finished
        return [-1, -1] # (Returning a list like [-1, -1] is safer if the function expects a List[int])