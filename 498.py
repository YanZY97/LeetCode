class Solution:
    def findDiagonalOrder(self, matrix: list) -> list:
        res = []
        if not matrix:
            return res

        def up(row, col):
            res.append(matrix[row][col])
            if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                return
            if row == 0 and not col == len(matrix[0]) - 1:
                return down(row, col + 1)
            if col == len(matrix[0]) - 1:
                return down(row + 1, col)
            row -= 1
            col += 1
            return up(row, col)

        def down(row, col):
            res.append(matrix[row][col])
            if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                return
            if col == 0 and not row == len(matrix) - 1:
                return up(row + 1, col)
            if row == len(matrix) - 1:
                return up(row, col + 1)
            row += 1
            col -= 1
            return down(row, col)

        up(0, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    res = solution.findDiagonalOrder(matrix)
    print(res)

