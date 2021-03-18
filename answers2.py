def bin_search(arr, n):
    """Binary search. Returns (idx, True) if the value is found,
       else returns the last index scanned and False"""
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid, True

    # return the last index scanned
    return mid, False

def mat_search(m, num):
    """Returns the index of num if contained in m, otherwise return -1
    
    m: matrix that have sorted rows and the columns.
    num: number to find in the matrix m
    
    """
    # since the values are row/column sorted
    # we can perform a binary search using the first value of each row first
    idx, found = bin_search([a[0] for a in m], num)
    # if num is in the first column, then we can already return the index
    if found:
        return (0, idx)

    # otherwise perform another binary search on the row and on the row before it
    for i in range(idx-1, idx+1):
        idx2, found = bin_search(m[i], num)
        if found:
            return (i, idx2)


    return -1

assert mat_search([[1,2,3], [4,5,6]], 2) == (0, 1)
assert mat_search([[1,2,3], [4,5,6], [7,8,9]], 5) == (1, 1)
assert mat_search([[1,2,3], [4,5,6], [7,8,9]], 9) == (2, 2)
assert mat_search([[1,2,3], [4,5,6], [7,8,9]], 1) == (0, 0)