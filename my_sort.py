def custom_sort(numbers):
    """
    Sorts a list of integers in ascending order using the Bubble Sort algorithm.
    Compares elements one-by-one and returns a new sorted list.
    
    Args:
        numbers: A list of integers.
        
    Returns:
        A tuple containing (the new sorted list, the number of comparisons made).
    """
    sorted_list = list(numbers)
    n = len(sorted_list)
    comparisons = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if sorted_list[j] > sorted_list[j + 1]:

                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                
    return sorted_list, comparisons