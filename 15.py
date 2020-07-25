class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = length - 1
            target = -nums[i]
            for j in range(i+1, length):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
        return res


if __name__ == '__main__':
    solution = Solution()
    a = [1,2,-2,-1]
    print(solution.threeSum(a))
