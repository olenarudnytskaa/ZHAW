"""
Context:
We have a set of patients, each with a severity score from 1 to 10. We want to sort them
so that higher-severity patients are prioritized for care. We'll implement a simple
insertion sort (descending order) and compare its performance against Python's built-in
sorted() function.

Exercise:
Resolve all the TODOs.

Note:
Insertion sort has O(n^2) worst-case complexity, while Python’s built-in sorted() uses
“Timsort” with a typical worst-case of O(n log n). For large lists, the built-in sort
should be significantly faster.
"""

import random
import time


def insertion_sort_desc(lst):
    """
    Insertion sort in descending order.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Shift elements that are smaller than key to one position ahead
        while j >= 0 and lst[j] < key:  # 'key < lst[j]' would result in ascending order
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


if __name__ == "__main__":
    # Generate a list of random severities (1 to 10) for 20,000 "patients"
    patient_severities = [random.randint(1, 10) for _ in range(20000)]

    # Make copies of the list so each test uses the same data
    list_for_insertion = patient_severities.copy()# TODO: Make copy of patient_severities
    list_for_builtin = patient_severities.copy()  # TODO: Make copy of patient_severities

    # 1) Time the custom insertion_sort_desc
    start_time = time.time()
    sorted_insertion = insertion_sort_desc(list_for_insertion) # TODO: Call the insertion_sort_desc function with the correct parameter.
    insertion_time = time.time() - start_time

    # 2) Time Python's built-in sort (also in descending order)
    start_time = time.time()
    sorted_builtin = sorted(list_for_builtin, reverse=True)  # TODO: Call the built-in 'sorted' function to sort the list 'list_for_builtin' in descending order (tip: sorted sorts in ascending order but there is a parameter 'reversed' that can be set to 'True')
    builtin_time = time.time() - start_time

    # Print times and a small sample of sorted results
    print(f"Insertion sort time: {insertion_time:.5f} seconds")
    print(f"Built-in sort time:  {builtin_time:.5f} seconds")

    # Verify correctness by comparing the first 10,000 entries
    print("\nFirst 10,000 from insertion sort:", sorted_insertion[:10000])
    print("First 10,000 from built-in sort:  ", sorted_builtin[:10000])
