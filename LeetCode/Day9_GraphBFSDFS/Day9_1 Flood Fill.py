# 2차원 배열을 주고 시작점을 주고 변경 해야하는 컬러 숫자를 주고 시작점 기준으로 시작점과 값이 같고 붙어 있는 애들을  주어진 컬러숫자로 변경하고 리턴한다 

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image




# 내가 처음 한거 

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        dict = {}
        row = int(len(image))
        col = int(len(image[0]))

        # 기존 값 저장하기 
        val = image[sr][sc]
        
        # 검사 해야하는 타겟 저장 리스트 
        check_lst = [[sr,sc]]

        # 동서남북 체크 
        dir = [[-1,0],[0,1],[1,0],[0,-1]]
        

        # 처음에 값 변경하기 
        image[sr][sc] = color

        while len(check_lst) != 0 :
            # 처음 시작점에서 동서남북 검사하기 
            target = check_lst.pop()
            for i in range(0,len(dir)):
                    # 동서남북 검사에서 2차원 배열 범위 벚어나지 않기
                if  (-1 < target[0]+dir[i][0] < row) and (-1 < target[1]+dir[i][1] < col)  and image[ target[0]+dir[i][0] ][ target[1]+dir[i][1] ] == val:

                    if ( target[0]+dir[i][0],target[1]+dir[i][1] )not in dict:
                        # 딕셔너리에 붙어있는 값 추가하기 
                        dict[ target[0]+dir[i][0] , target[1]+dir[i][1] ] = val
                        # 기존 배열에 컬러 변경 
                        
                        image[target[0]+dir[i][0]][target[1]+dir[i][1]] = color
                        # 검사 해야 하는 친구 추가하기
                        check_lst.append([ target[0]+dir[i][0] , target[1]+dir[i][1] ]) 
        return image



