class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split('/')
        res_l = []
        for item in l:
            if item == '':
                continue
            elif item == '.':
                continue
            elif item == '..':
                try:
                    res_l.pop()
                except:
                    continue
            else:
                res_l.append(item)
        return '/' + '/'.join(res_l)


if __name__ == '__main__':
    solution = Solution()
    s = "/home/"
    res = solution.simplifyPath(s)
    print(res)
