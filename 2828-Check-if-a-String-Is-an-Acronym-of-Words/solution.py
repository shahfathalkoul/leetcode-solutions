class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        k = ""
        for i in words:
            k += i[0]
        return k == s
        