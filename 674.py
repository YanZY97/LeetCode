class Solution:
    # def __init__(self):
    #     self.result = list()
    #
    # def findLengthOfLCIS(self, nums: list) -> int:
    #     if len(nums) <= 1:
    #         return len(nums)
    #     self.search(nums, 0)
    #     res = len(self.result) if len(self.result) > 1 else 1
    #     return res
    #
    # def search(self, nums, pos):
    #     que = [nums[pos]]
    #     for i in range(pos+1, len(nums)):
    #         if que[-1] < nums[i]:
    #             que.append(nums[i])
    #             if len(que) > len(self.result):
    #                 self.result = que
    #         else:
    #             return self.search(nums, i)
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [2,1,2,2,2]
    print(solution.findLengthOfLCIS(nums))
