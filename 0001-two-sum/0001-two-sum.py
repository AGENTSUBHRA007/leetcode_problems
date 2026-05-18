class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # val : index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is already in our map, we found the pair!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the current number and its index
            seen[num] = i