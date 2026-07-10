#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    unique_numbers = set()
    total = 0

    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.add(num)
            total += num

    return total
