class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Loop through every index and element in the list
        for i in range(len(nums)):
            # If the current element matches our target, return its index
            if nums[i] == target:
                return i
                
        # If the loop finishes and we never found the target, return -1
        return -1