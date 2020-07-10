class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        return len(haystack.split(needle)[0]) if len(haystack.split(needle)) > 1 else -1


if __name__ == '__main__':
    solution = Solution()
    haystack = "hello"
    needle = "e"
    res = solution.strStr(haystack, needle)
    print(res)
