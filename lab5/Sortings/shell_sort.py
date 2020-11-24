def shell_sort(array):
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
if __name__ == "__main__":
    nums = [-2, -1, 0, 1, 0, -1, -2]
    shell_sort(nums)
    print(nums)