def remove_duplicates(array):
    if len(array) == 0:
        return 0

    unique_ptr = 0  # Penunjuk untuk elemen unik
    for i in range(1, len(array)):
        if array[i] != array[unique_ptr]:
            unique_ptr += 1
            array[unique_ptr] = array[i]

    return unique_ptr + 1  # Panjang subarray tanpa duplikat

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4