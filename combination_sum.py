class Solution:
    def combinationSum(self, candidates, target: int):
        dp = [[] for _ in range(target+1)] # empty list of lists

        # Create subcombination lists
        for c in candidates:
            for t in range(1, target + 1):
                if c > t: continue 
                if c == t: dp[t].append([c]) # perfect match
                for l in dp[t-c]: # imperfect matches
                    dp[t].append(l+[c])

        return dp

# https://www.youtube.com/watch?v=2_58CA1fyn4
candidates = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))