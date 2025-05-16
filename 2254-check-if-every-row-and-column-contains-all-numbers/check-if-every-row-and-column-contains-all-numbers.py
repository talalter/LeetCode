class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in range(n):
            n_set = set([n+1 for n in range(n)])
            for col in range(n):
                if matrix[row][col] in n_set:
                    n_set.remove(matrix[row][col])
                else:
                    return False

        for row in range(n):
            n_set = set([n+1 for n in range(n)])
            for col in range(n):
                if matrix[col][row] in n_set:
                    n_set.remove(matrix[col][row])
                else:
                    return False            
        
        return True