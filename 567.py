class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return True
        if len(s1) > len(s2):
            return False
        idx = 0
        while idx + len(s1) <= len(s2):
            lookup = s2[idx:idx + len(s1)]
            for i in s1:
                lookup = lookup.replace(i, '', 1)
            if len(lookup) == 0:
                return True
            idx += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    s1 = 'pewkw234w1'
    s2 = 'pww1234kew'
    print(solution.checkInclusion(s1, s2))
