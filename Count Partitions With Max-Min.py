class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1
        prefix_sum = [0] * (n + 2)
        prefix_sum[1] = 1
        
        min_q = deque()
        max_q = deque()
        left = 0
        
        for i in range(1, n + 1):
            val = nums[i-1]
            
            while min_q and nums[min_q[-1]] >= val:
                min_q.pop()
            min_q.append(i-1)
            
            while max_q and nums[max_q[-1]] <= val:
                max_q.pop()
            max_q.append(i-1)
            
            while nums[max_q[0]] - nums[min_q[0]] > k:
                left += 1
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()
            
            dp[i] = (prefix_sum[i] - prefix_sum[left]) % MOD
            prefix_sum[i+1] = (prefix_sum[i] + dp[i]) % MOD
            
        return dp[n]
