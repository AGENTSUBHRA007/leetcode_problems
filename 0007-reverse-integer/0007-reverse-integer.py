class Solution:
    def reverse(self, x: int) -> int:
        
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)
            
        d = x
        res_sum = 0 
        
        
        while d > 0:
            rem = d % 10
            res_sum = (res_sum * 10) + rem
            d = d // 10
            
        
        if is_negative:
            res_sum = -res_sum
            
        
        if res_sum < -2**31 or res_sum > 2**31 - 1:
            return 0
            
        return res_sum