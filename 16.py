import math


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        ans_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(ans_sum - target):
                    ans_sum = curr_sum
                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    return target
        return ans_sum


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 2, -2, -3]
    target = 1
    print(solution.threeSumClosest(nums, target))
