from collections import deque
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.res = False
        def dfs(index):
            res = False
            def dfs_helper(index, visited):
                nonlocal res 
                if index >= len(nums) - 1:
                    res = True
                    return True

                if len(visited) == len(nums):
                    return 

                visited.add(index)
                for jump in range(1, nums[index] + 1):
                    maxJump = index + jump
                    if maxJump >= len(nums) - 1:
                        res = True
                        return 
                    if maxJump not in visited and dfs(maxJump):
                        return True
                return False
            res = dfs_helper(index, set())
            return res
        
        def bfs(index):
            queue = deque([index])
            visited = set([index])
            
            while queue:
                currPos = queue.popleft()
                if currPos >= len(nums) - 1:
                    return True
                maxJump = currPos + nums[currPos] + 1
                for jump in range(currPos + 1, maxJump):
                    if jump >= len(nums):
                        return True
                    if jump not in visited and jump < len(nums):
                        queue.append(jump)
                        visited.add(jump)
            return False
        # self.res = bfs(0)
        self.res = dfs(0)
        return self.res

nums = [2, 3, 1, 1, 4]
nums = [1, 1, 1, 0]
# nums = [0]
# nums = [3,2,1,0,4]
# nums = [2, 0]
# nums = [2, 5, 0, 0]
# nums = [2, 5, 0, 0, 0, 0, 0, 0]
# nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(Solution().canJump(nums))