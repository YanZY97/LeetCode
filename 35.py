class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        def search(nums: list, left, right, target):
            if right >= left:
                mid = int(left + (right - left) // 2)
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    return search(nums, mid + 1, right, target)
                elif target < nums[mid]:
                    return search(nums, left, mid - 1, target)
            else:
                return left

        return search(nums, 0, len(nums) - 1, target)


