class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        ans = []

        for i in range(n):
            degree = 0

            for j in range(n):
                degree += matrix[i][j]

            ans.append(degree)

        return ans
        