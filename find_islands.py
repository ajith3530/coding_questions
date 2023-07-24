class Solution:
    def numIslands(self, grid):
        islands_count = 0

        if len(grid) == 0:
            return islands_count

        total_rows = len(grid)
        total_columns = len(grid[0])
        def bfs(row, column, grid):
            if grid[row][column] == "1":
                grid[row][column] = "2"
                
                bfs(min(total_rows-1, row+1), column, grid)
                bfs(max(0, row-1), column, grid)
                bfs(row, min(column+1, total_columns-1), grid)
                bfs(row, max(column-1, 0), grid)

        for row in range(total_rows):
            for column in range(total_columns):
                if grid[row][column] == "1":
                    islands_count +=1

                    bfs(row, column, grid)
        return islands_count


input_matrix = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(Solution().numIslands(input_matrix))
