class Solution:
    def scoreOfString(self, s: str) -> int:
        initial = ord(s[0])
        sum1 = 0
        for i in s[1:]:
            v = ord(i)
            sum1 += abs(initial - v)
            # print(sum1)
            initial = v
        return sum1
  
            
        