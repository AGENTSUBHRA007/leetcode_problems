class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
     
        def findBound(is_left: bool) -> int:
            start = 0
            end = len(nums) - 1
            bound = -1
            
            while start <= end:
                mid = (start + end) // 2
                
                if nums[mid] == target:
                    bound = mid 
                    if is_left:
                        end = mid - 1   
                    else:
                        start = mid + 1 
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
                    
            return bound
        
       
        first_pos = findBound(is_left=True)
        last_pos = findBound(is_left=False)
        
        return [first_pos, last_pos]