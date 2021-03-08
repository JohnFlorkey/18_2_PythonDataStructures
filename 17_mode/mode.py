def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    item_dict = {num: nums.count(num) for num in nums}
    values = item_dict.values()
    max_value = 0
    for value in values:
        if value > max_value:
            max_value = value
    for (k,v) in item_dict.items():
        if v == max_value:
            return k