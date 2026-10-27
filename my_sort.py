def selection_sort(numbers):
    """
    Sorts a list of numbers in ascending order in-place using Selection Sort.
    
    Args:
        numbers: A list of integers to be sorted.
        
    Returns:
        The total number of comparisons made during the sorting process.
    """
    comparisons = 0
    n = len(numbers)
    
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if numbers[j] < numbers[min_index]:
                min_index = j
 
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        
    return comparisons