"""
Insertion Sort

Its also known as inplace sorting,


Stable Sorting:  Order must be preserved if the elements are same in the array, its the property of a sorting algorithm.
Reference Documents:

"""


def insertion_sort(array):
    """

    :param array:
    :return:
    """
    len_array = len(array)
    if len_array <= 1:
        return array

    # Iterate from second element of the list
    for i in range(1, len(array)):

        current_value = array[i]
        j = i - 1

        # Go backwards and till u find a element smaller than the current value in a sub array.
        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_value

    return array


assert insertion_sort([6, 5, 3, 1, 8, 7, 2, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]
