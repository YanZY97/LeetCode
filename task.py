import time


class Solution1:
    def __init__(self):
        self.hash_table = {}
        self.count = 0
        for i in range(0, 10):
            self.hash_table.update({str(i): [str(abs(i-j)) for j in range(0, 10)]})

    def count_lucky(self, l):
        for i in range(l):
            if self.is_lucky(i):
                self.count += 1
                # print(i)
        return self.count

    def is_lucky(self, num):
        num_str = str(num)
        if len(num_str) == 1:
            return num_str == '7'
        tmp = ''
        for i in range(len(num_str)-1):
            tmp += self.hash_table[num_str[i]][int(num_str[i+1])]
        num_str = tmp
        return self.is_lucky(num_str)


class Solution2:
    def __init__(self):
        self.hash_table = {}
        self.count = 0
        for i in range(0, 10):
            value = []
            for j in range(0, 10):
                if j + i < 10:
                    value.append([str(j), str(j+i)])
                    if not i == 0:
                        value.append([str(j+i), str(j)])
            self.hash_table.update({str(i): value})
        print(self.hash_table)

    def find_lucky(self, num, target):
        tmp = ''
        tmp_list = []
        num_str = str(num)
        for i in range(len(num_str)):
            for com in self.hash_table[num_str[i]]:
                if com[0] == '0':
                    continue
                tmp += com[0]
                tmp += com[1]
                for j in range(1, len(num_str)):
                    for com1 in self.hash_table[num_str[j]]:
                        pass


if __name__ == '__main__':
    # start_time = time.time()
    # solution = Solution1()
    # res = solution.count_lucky(100000)
    # print(res)
    # print(time.time() - start_time)

    solution2 = Solution2()
    solution2.find_lucky(7, (0, 10000))

