

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        # Helper function jo pairs ka product dhoondhega dusre array ke squares ki dictionary mein
        def countPairs(target_squares_dict, nums_arr):
            pairs_count = 0
            n = len(nums_arr)
            # Har ek possible pair (j, k) ka loop jahan j < k
            for j in range(n):
                for k in range(j + 1, n):
                    product = nums_arr[j] * nums_arr[k]
                    # Agar yeh product kisi ke square ke barabar hai, toh count add karo
                    if product in target_squares_dict:
                        pairs_count += target_squares_dict[product]
            return pairs_count

        # Step 1: Dono arrays ke elements ke squares ka frequency map (dictionary) banaya
        # Counter loop chala kar automatically {square: kitni_baar_aaya} store kar leta hai
        sq1 = Counter(x * x for x in nums1)
        sq2 = Counter(x * x for x in nums2)
        
        # Step 2: Type 1 + Type 2 dono ke sahi triplets ka total sum nikala
        type1 = countPairs(sq1, nums2) # nums1[i]^2 == nums2[j] * nums2[k]
        type2 = countPairs(sq2, nums1) # nums2[i]^2 == nums1[j] * nums1[k]
        
        return type1 + type2