def shell_sort(data):
    n = len(data)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = data[i]
            j = i
            while j >= interval and data[j - interval] > temp:
                data[j] = data[j - interval]
                j -= interval

            data[j] = temp
        interval //= 2
if __name__ == "__main__":
    nums = [-2, -1, 0, 1, 0, -1, -2]
    shell_sort(nums)
    print(nums)