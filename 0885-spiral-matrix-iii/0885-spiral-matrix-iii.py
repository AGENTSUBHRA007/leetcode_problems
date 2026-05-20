class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        total_elements = rows * cols
        
        r, c = rStart, cStart
        steps = 1  
        
        
        result.append([r, c])
        
        
        while len(result) < total_elements:
            
            
            for _ in range(steps):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                    
            
            for _ in range(steps):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            
            steps += 1
            
            
            for _ in range(steps):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                    
            
            for _ in range(steps):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            
            steps += 1
            
        return result