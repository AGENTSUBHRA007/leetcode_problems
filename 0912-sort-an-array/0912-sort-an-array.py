class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums) // 2
        
       
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        
        return self.merge(left_half, right_half)
        
    def merge(self,left:List[int],right:List[int])->List[int]:
        sorted_arr = []
        i, j = 0, 0  
        
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
                
        
        while i < len(left):
            sorted_arr.append(left[i])
            i += 1
        while j < len(right):
            sorted_arr.append(right[j])
            j += 1
            
        return sorted_arr
        