import numpy as np


# 审错题，*取代任意长度任意字符
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        cell = np.zeros((len(s), len(p)))
        if '*' not in p and len(s) != len(p):
            return False
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '.':
                    cell[i][j] = 1 if not i * j else cell[i-1][j-1] + 1
                else:
                    if i == 0:
                        cell[i][j] = cell[i][j-1] if j != 0 else 0
                    elif j == 0:
                        cell[i][j] = cell[i-1][j] if i != 0 else 0
                    cell[i][j] = max(cell[i-1][j], cell[i][j-1])
        maxlen = cell[-1][-1]
        if cell[0][0] != 0 or p[0] == '*':
            if maxlen == len(''.join(p.split('*'))):
                return True
        return False


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s  # 结束条件
        first_match = (len(s) > 0) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cell = np.zeros((len(s), len(p)))
        maxlen = 0
        start_point = 0
        for i in range(len(s)):
            for j in range(start_point, len(p)):
                if p[j] == s[i] or p[j] == '.':
                    maxlen += 1
                    start_point = j
                    if j+1 < len(p) and p[j+1] == '*':
                        cell[i][j+1] = maxlen
                        break
                    else:
                        cell[i][j] = maxlen
                        start_point += 1
                        break
        print(cell)

        if max(cell[:, -1]) == len(s):
            return True
        elif maxlen == len(s):
            for i in range(1, len(p)-start_point-1):
                if s[-i] != p[-i]:
                    return False
            return True
        else: return False


if __name__ == '__main__':
    s = "aaa"
    p = "aaaa"
    solution = Solution()
    print(solution.isMatch(s, p))

