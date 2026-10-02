class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            sum1 = 1
            for i in range(1,len(s)):
                sum1 += int(s[i]) + int(s[i - 1])
            s = str(sum1)
        return s
        
        