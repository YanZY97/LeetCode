class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        res = []
        left_point = 2 if 4 <= len(s) <= 8 else len(s) - 6
        right_point = 6 if len(s) >= 8 else len(s) - 2
        for point in range(left_point, right_point+1):
            part1 = s[0:point]
            part2 = s[point:]
            left_point1 = 1 if len(part1) <= 4 else len(part1) - 3
            right_point1 = 3 if len(part1) >= 4 else len(part1) - 1
            left_point2 = 1 if len(part2) <= 4 else len(part2) - 3
            right_point2 = 3 if len(part2) >= 4 else len(part2) - 1
            for i in range(left_point1, right_point1 + 1):
                for j in range(left_point2, right_point2 + 1):
                    part11 = part1[0:i]
                    if int(part11) > 255 or (len(part11) > 1 and part11[0] == "0"):
                        continue
                    part12 = part1[i:]
                    if int(part12) > 255 or (len(part12) > 1 and part12[0] == "0"):
                        continue
                    part21 = part2[0:j]
                    if int(part21) > 255 or (len(part21) > 1 and part21[0] == "0"):
                        continue
                    part22 = part2[j:]
                    if int(part22) > 255 or (len(part22) > 1 and part22[0] == "0"):
                        continue
                    res.append(part11 + '.' + part12 + '.' + part21 + '.' + part22)
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "255255255255"
    res = solution.restoreIpAddresses(s)
    print(res)
