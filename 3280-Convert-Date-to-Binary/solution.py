class Solution:
    def convertDateToBinary(self, date: str) -> str:
        k = ""
        list1 = date.split("-")
        for i in range(len(list1)):
            k += bin(int(list1[i]))
            k += "-"
        return k
        