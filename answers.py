def max_cont_sum(arr):
    """Given an array A of integers (both positive and negative integers),
       returns the maximum contiguous sum.
    """
    # store the highest sum and compare it with each additional item
    high_sum = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum = curr_sum + arr[i]
        # reset if we go below zero
        if curr_sum < 0:
            curr_sum = 0

        # update the sum if the current sum is higher
        elif high_sum < curr_sum:
            high_sum = curr_sum
    return high_sum

assert max_cont_sum([1, 2, -3, 5]) == 5
assert max_cont_sum([1, 2, 3, -4, 10]) == 12
assert max_cont_sum([1, 2, -3, -5, 1]) == 3
