class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        dp[0][0] = 0
        
        for i in range(m):
            new_dp = [[-1] * (k + 1) for _ in range(n)]
            for j in range(n):
                cell_val = grid[i][j]
                cost_inc = 1 if cell_val > 0 else 0
                score_inc = cell_val
                
                for c in range(cost_inc, k + 1):
                    res = -1
                    
                    if i > 0:
                        res = max(res, dp[j][c - cost_inc])
                    
                    if j > 0:
                        res = max(res, new_dp[j - 1][c - cost_inc])
                    
                    if i == 0 and j == 0:
                        res = 0
                        
                    if res != -1:
                        new_dp[j][c] = res + score_inc
            dp = new_dp
            
        ans = max(dp[n - 1])
        return ans if ans != -1 else -1
