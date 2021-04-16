def merge_sort(arr):
    len_arr = len(arr)

    if len_arr >= 1:
        left = arr[:len_arr/2]
        right = arr[len_arr/2:]

        merge_sort(left)

        merge_sort(right)

        i = j = k = 0



merge_sort([3, 1, 8, 4, 2, 5, 0])
