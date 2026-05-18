class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        triplets = set()
        nums.sort()
        
        for i in range(len(nums)):
            
            if nums[i] > 0:
                break
                
            
            seen = set()
            
           
            for j in range(i + 1, len(nums)):
              
                complement = -(nums[i] + nums[j])
                
                
                if complement in seen:
                    
                    triplets.add((nums[i], complement, nums[j]))
                
               
                seen.add(nums[j])
                
        
        return [list(t) for t in triplets]