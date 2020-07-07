class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == '__main__':
    solution = Solution()
    s = "a good   exampleas df dsaf 1 23 ds    "
    res = solution.reverseWords(s)
    print(res)
