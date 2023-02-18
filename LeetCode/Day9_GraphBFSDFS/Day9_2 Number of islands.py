# 1'(육지)와 '0'(물)의 지도를 나타내는 m x n 2D 이진 그리드가 주어지면 섬의 수를 반환합니다.

# 섬은 물로 둘러싸여 있고, 인접한 땅들이 수평 또는 수직으로 연결되어 형성된다. 그리드의 네 모서리가 모두 물로 둘러싸여 있다고 가정할 수 있습니다.Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.




# 이건 루이꺼 하지만 매우니르지만 메모리는 가장적게씀 
class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        n = len(grid[0])
        tmp = ["1" in row for row in grid]
        while True in tmp:
            count += 1
            x = tmp.index(True)
            y = grid[x].index("1")
            queue = [[x,y]]
            while len(queue) > 0:
                [x,y] = queue.pop(0)
                if grid[x][y] == "1":
                    grid[x][y] = "0"
                    if grid[max(0, x-1)][y] == "1": #up
                        queue.append([max(0, x-1),y])

                    if grid[min(x+1, m-1)][y] == "1": #down
                        queue.append([min(x+1, m-1),y])

                    if grid[x][max(0,y-1)] == "1": #left
                        queue.append([x,max(0,y-1)])

                    if grid[x][min(n-1,y+1)] == "1": #right
                        queue.append([x,min(n-1,y+1)])
            tmp = ["1" in row for row in grid]
        return count

# 내가 한거 문제 푸는거 성공했지만 메모리하고 속도 평균 .. 다른예제 아직 보지 않음
        # dict = {}
        # dir = [[-1,0],[0,1],[1,0],[0,-1]] 
        # row = int(len(grid))
        # col = int(len(grid[0]))
        # count = 0
        # lst = []


        #     # 동서남북 계산
        # def cal(cp_row,cp_col,count):
        #     if (cp_row,cp_col) not in dict:
        #         dict[cp_row,cp_col] = "1"
        #         lst.append([cp_row,cp_col])

        #         while len(lst) !=0 :
        #             land = lst.pop(0)
        #             for i in range(0,len(dir)) :        
        #                 if (0 <= land[0] + dir[i][0] < row) and (0 <= land[1] + dir[i][1] < col) and grid[land[0] + dir[i][0]][land[1] + dir[i][1]] == "1":
        #                     if (land[0] + dir[i][0] , land[1] + dir[i][1]) not in dict:
        #                         dict[ land[0] + dir[i][0] , land[1] + dir[i][1] ] = "1"
        #                         lst.append([land[0] + dir[i][0],land[1] + dir[i][1]])

        #         return count +1
        #     return count

        # # 배열 돌기 
        # for i in range(0,len(grid)):
        #     for j in range(0,len(grid[0])):
        #         if  grid[i][j] == "1":               
        #             count = cal(i,j,count)
        # return count


