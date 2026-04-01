from functools import cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def solve(z, o, last):
            # Base Case: No more digits to place
            if z == 0 and o == 0:
                return 1
            
            res = 0
            if last == 0:
                # We just placed 0s, now we must place 1s
                # We can place k ones, where 1 <= k <= min(o, limit)
                for k in range(1, min(o, limit) + 1):
                    res = (res + solve(z, o - k, 1)) % MOD
            else:
                # We just placed 1s (or are starting), now we must place 0s
                # We can place k zeros, where 1 <= k <= min(z, limit)
                for k in range(1, min(z, limit) + 1):
                    res = (res + solve(z - k, o, 0)) % MOD
            return res

        # We can start by placing a block of 0s or a block of 1s.
        # solve(z, o, 0) means the "previous" block was 0, so it forces a 1.
        # To allow starting with either, we call both from an empty state.
        
        # Initial calls:
        # Placing a block of 0s first:
        ans_start_zero = 0
        for k in range(1, min(zero, limit) + 1):
            ans_start_zero = (ans_start_zero + solve(zero - k, one, 0)) % MOD
            
        # Placing a block of 1s first:
        ans_start_one = 0
        for k in range(1, min(one, limit) + 1):
            ans_start_one = (ans_start_one + solve(zero, one - k, 1)) % MOD
            
        # However, the recursive structure solve(z, o, last) already handles 
        # the "next block" logic. A simpler entry point:
        
        @cache
        def dp(z, o, last):
            if z == 0 and o == 0: return 1
            ans = 0
            if last == 1: # Last was 1, must place 0
                for k in range(1, min(z, limit) + 1):
                    ans = (ans + dp(z - k, o, 0)) % MOD
            else: # Last was 0, must place 1
                for k in range(1, min(o, limit) + 1):
                    ans = (ans + dp(z, o - k, 1)) % MOD
            return ans

        # Result is starting with a block of 0 OR starting with a block of 1
        return (dp(zero, one, 0) + dp(zero, one, 1)) % MOD