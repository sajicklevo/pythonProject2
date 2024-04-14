class Solution:
    def permute(self, nums):
        result = []
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return result
solution = Solution()
nums=[1,2,3]
print(solution.permute(nums))