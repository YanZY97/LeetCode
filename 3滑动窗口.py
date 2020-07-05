# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = 0
#         flag = 0
#         for indexa, a in enumerate(s):
#             start_index = indexa
#             for index, i in enumerate(s[indexa+1:]):
#                 if i == a:
#                     flag = 1
#                     l = index - start_index+1 if index - start_index+1 > l else l
#                     start_index = index+1
#         return l if flag == 1 else len(s)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lookup = list()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            val = s[i]
            if not val in lookup:
                lookup.append(val)
                cur_len += 1
            else:
                index = lookup.index(val)
                lookup = lookup[index+1:]
                lookup.append(val)
                cur_len = len(lookup)
            if cur_len > max_len:
                max_len = cur_len
        return max_len


if __name__ == '__main__':
    solution = Solution()
    input = 'pwwkew'
    print(solution.lengthOfLongestSubstring(input))
