def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    list = [1,3,13,7,9,2]
    a = sum(list)
    b = count(list)
    c = max(list)
    d = quick_sort(list)
    print(d)
