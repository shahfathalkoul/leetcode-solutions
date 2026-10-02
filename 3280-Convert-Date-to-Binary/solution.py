class Solution:
    def convertDateToBinary(self, date: str) -> str:
        k = ""
        list1 = date.split("-")
        for i in range(len(list1)):
            z = bin(int(list1[i]))
            k += z[2 :]
            k += "-"
        return k
        