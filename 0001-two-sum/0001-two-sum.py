class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers we've seen: {number: its_index}
        seen = {} 
        
        # enumerate() gives us both the index (i) and the number itself (num)
        for i, num in enumerate(nums):
            
            # The number we need to find to hit our target
            needed = target - num
            
            # Did we already see the number we need?
            if needed in seen:
                # Yes! Return the index of the needed number, and our current index
                return [seen[needed], i]
            
            # No? Add our current number and its index to the dictionary so 
            # future numbers can find it.
            seen[num] = i