class Solution:
    def pivotIndexPos(self, nums: list) -> int:
        if len(nums) == 0:
            return -1
        left_ptr = 0
        right_ptr = len(nums) - 1
        sum_left = nums[0]
        sum_right = nums[-1]
        while not right_ptr <= left_ptr + 2:
            if sum_left < sum_right:
                left_ptr += 1
                sum_left += nums[left_ptr]
            else:
                right_ptr -= 1
                sum_right += nums[right_ptr]
        res = left_ptr + 1 if sum_left == sum_right else -1
        if sum_right == 0 and nums[0] == 0:
            res = 0
        return res

    def pivotIndex(self, nums: list) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1