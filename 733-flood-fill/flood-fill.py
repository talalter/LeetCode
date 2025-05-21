from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:        

        starting_color = image[sr][sc]
        if starting_color == color:
            return image
            
        rows = len(image)
        cols = len(image[0])
        directions = [[1, 0], [-1,0], [0,1], [0, -1]]
        queue = deque([(sr, sc)])

        while queue:
            row, col = queue.popleft()
            if image[row][col] == starting_color:
                image[row][col] = color
                for dr, dc in directions:
                    new_row, new_col = dr + row, dc + col
                    if 0 <= new_row < rows and 0<= new_col < cols:
                        queue.append((new_row, new_col))
        
        return image