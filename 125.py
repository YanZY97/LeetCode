import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.split(r'[^A-Z0-9]', s.upper()))
        return s[::-1] == s


if __name__ == '__main__':
    input = "asdffdsa"
    solution = Solution()
    print(solution.isPalindrome(input))
