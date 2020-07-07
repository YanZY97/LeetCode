class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if s == s[::-1]:
    #         return s
    #     lookup = s[0]
    #     start_idx = 0
    #     while not start_idx + len(lookup) >= len(s):
    #         if s[start_idx:start_idx + len(lookup) + 1] == s[start_idx:start_idx + len(lookup) + 1][::-1]:
    #             lookup = s[start_idx:start_idx + len(lookup) + 1]
    #         if not start_idx == 0:
    #             if s[start_idx:start_idx+len(lookup)] == s[start_idx:start_idx+len(lookup)][::-1]:
    #                 if start_idx + len(lookup) >= len(s):
    #                     break
    #                 if s[start_idx-1] == s[start_idx + len(lookup)]:
    #                     lookup = s[start_idx-1:start_idx+len(lookup)+1]
    #                     start_idx -= 1
    #                     continue
    #         start_idx += 1
    #     return lookup
    def spread(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd = self.spread(s, i, i)
            palindrome_even = self.spread(s, i, i + 1)
            res = max(palindrome_odd, palindrome_even, res, key=len)
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "hsS1ascsfqooooor"
    res = solution.longestPalindrome(s)
    print(res)
