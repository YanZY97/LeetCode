def add(nums, target):
    for i in range(len(nums)):
        a = nums.pop()
        for index, b in enumerate(nums):
            if a+b == target:
                return index, len(nums)


if __name__ == '__main__':
    a, b = add([2, 7, 11, 15], 9)
    print(a, b)
