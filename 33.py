class Solution:
    def search(self, nums: list, target: int) -> int:
        if len(nums) < 1:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pos = l
        l = 0 if target > nums[-1] else pos
        r = pos-1 if target > nums[-1] else len(nums) - 1
        return self.binarySearch(nums, l, r, target)

    def binarySearch(self, arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid - 1, x)
            else:
                return self.binarySearch(arr, mid + 1, r, x)
        else:
            return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    solution = Solution()
    print(solution.search(nums, target))
