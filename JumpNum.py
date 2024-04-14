
class Solution:
    def Jump(self,nums):
        max_boom = 0
        for i in range(len(nums)-1):
            if i>max_boom:
                return False
            max_boom=max(max_boom,i+nums[i])
            if max_boom>=len(nums)-1:
                return True
solution=Solution()
nums=[2,3,1,1,4]
print(solution.Jump(nums))

