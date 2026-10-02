class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        i = 0
        g = len(s) - 1
        while i < (len(s)//2):
            s[i], s[g] = s[g], s[i]
            i += 1
            g -= 1
        
        