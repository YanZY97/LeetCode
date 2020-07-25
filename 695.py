class Solution:
    def __init__(self):
        self.area = 0
        self.max_area = 0

    def maxAreaOfIsland(self, grid: list) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.area = 0
                self.findNeighbor([row, col], grid)
        return self.max_area

    def findNeighbor(self, location, grid):
        col, row = location[1], location[0]
        if grid[row][col] == 0:
            return
        self.area += 1
        neighbor = []
        if not col == 0 and grid[row][col-1] == 1:
            neighbor.append([row, col-1])
        if not col == len(grid[0]) - 1 and grid[row][col+1] == 1:
            neighbor.append([row, col+1])
        if not row == 0 and grid[row-1][col] == 1:
            neighbor.append([row-1, col])
        if not row == len(grid) - 1 and grid[row+1][col] == 1:
            neighbor.append([row+1, col])
        grid[row][col] = 0
        if self.area > self.max_area:
            self.max_area = self.area
        if not len(neighbor) == 0:
            for point in neighbor:
                self.findNeighbor(point, grid)
            return


if __name__ == '__main__':
    solution = Solution()
    a = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(solution.maxAreaOfIsland(a))
