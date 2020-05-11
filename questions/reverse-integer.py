#Given a 32-bit signed integer, reverse digits of an integer.
#-123 -> -321
#120 -> 21
#[−231,  231 − 1]
#‭2**31-1 = ‭2,147,483,647‬
#result must also be in range 
#2147483642 -> 0
#-2147483642 -> 0
#python reverse-integer.py 123 
import sys

#if running from cmd
#input = sys.argv[1]
input = 123
input = 234
input = 2147483648
input = -2147483649
#input = -123
#input = 120
#input = 1
input = 0
input = -10
input = 100

class Solution:
    def reverse(self, x: int) -> int:
        print(x)
        if x >= 2147483647:
            return 0
        if x <= -2147483648:    
            return 0
        if x == 0:
            return 0    
        strinput = str(x)
        if strinput[0] == '-':
            revstr = '-'
            strinput=strinput[1: len(strinput)]
        else:
            revstr = ''
        #print(strinput)    
        strinput=strinput.rstrip('0')
        #print(strinput)    
        for i in range(len(strinput)-1, -1, -1):
            revstr = revstr + strinput[i]
        if int(revstr) >= 2147483647:
            return 0
        if int(revstr) <= -2147483648:    
            return 0
        return revstr

solution = Solution()
print(solution.reverse(input))
        