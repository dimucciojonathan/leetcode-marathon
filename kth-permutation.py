import math

class Solution:
    def __init__(self):
        return
    
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1 # list index starts from 0
        nums = list(range(1,n+1))
        sol =  ''

        # Get other indexes
        while len(nums) > 0:
            index = k // math.factorial(n-1)
            sol += str(nums[index])
            nums.pop(index)

            k = k % math.factorial(n-1)
            n -= 1
        return sol

        
sol = Solution()
print(sol.getPermutation(n=4,k=4))