class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        ptr = 0
        res = ""
        if not strs:
            return res
        if len(strs) == 1:
            return strs[0]
        while not strs[0] == "":
            for i in range(1, len(strs)):
                try:
                    if not strs[i][ptr] == strs[0][ptr]:
                        return res
                except:
                    return res
            res += (strs[0][ptr])
            ptr += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    matrix = ["a"]
    res = solution.longestCommonPrefix(matrix)
    print(res)