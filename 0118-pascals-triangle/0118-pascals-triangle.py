class Solution:
    def generate(self, numRows: int):
        triangle = []

        for i in range(numRows):
            # Start every row with 1
            row = [1] * (i + 1)

            # Calculate the middle elements
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle