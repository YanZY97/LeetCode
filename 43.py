class Solution:
    def multiply1(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = 0
        for idx2, i in enumerate(num2):
            temp = 0
            for idx1, j in enumerate(num1):
                temp += int(i) * int(j) * 10**idx1
            res += temp * 10**idx2
        return str(res)

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [int(0)] * (len(num1) + len(num2))
        for idx2, i in enumerate(num2):
            for idx1, j in enumerate(num1):
                sum = res[idx1 + idx2 + 1] + int(i) * int(j)
                res[idx1 + idx2 + 1] = sum % 10
                res[idx1 + idx2] += sum // 10
        return res


if __name__ == '__main__':
    solution = Solution()
    s1 = '123'
    s2 = '456'
    print(solution.multiply(s1, s2))
