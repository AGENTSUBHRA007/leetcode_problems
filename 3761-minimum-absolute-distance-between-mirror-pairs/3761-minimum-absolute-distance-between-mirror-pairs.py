class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Dictionary format: { reversed_version_of_nums_i : index_i }
        seen = {}
        min_dist = -1
        
        for j in range(len(nums)):
            current_val = nums[j]
            
            # Step 1: Check if the current value matches a previously reversed number
            # Because we stored keys as reverse(nums[i]), if current_val is in seen,
            # then reverse(nums[i]) == nums[j] is perfectly true!
            if current_val in seen:
                distance = j - seen[current_val]
                if min_dist == -1 or distance < min_dist:
                    min_dist = distance
            
            # Step 2: Mathematically reverse the current value BEFORE storing it
            temp = current_val
            rev = 0
            while temp > 0:
                rev = (rev * 10) + (temp % 10)
                temp //= 10
                
            # Step 3: Record it. We use 'rev' as the key.
            # If rev is already in seen, we overwrite it with 'j' because a later index
            # will always give a smaller absolute distance for any future matches.
            seen[rev] = j
            
        return min_dist