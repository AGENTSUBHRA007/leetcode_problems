class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
       
        for i in range(2, n - 1):
            
           
            d = n
            convert_string = ""
            
         
            while d > 0:
                rem = d % i
                convert_string += str(rem)
                d = d // i
                
           
            if convert_string != convert_string[::-1]:
                return False
                
       
        return True