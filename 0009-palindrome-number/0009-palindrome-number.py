class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum=0
        d=x
        if x<0:
            return False
        while(d>0):
            rem =d%10
            sum=(sum*10)+rem
            d=d//10

        if x==sum:
           return True
        else:
          return False