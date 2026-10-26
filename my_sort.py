# Idea: to compare given i with each following number in a list. Due to n-tries, an ordered list will be constracted 


def selection_sort(numbers):
    """Sorts a list of numbers in ascending order and returns a number of comparisons"""
    
    comparisons = 0                                                     # counts comparisons
    n = len(numbers)
    for i in range(n - 1):
        smallest = i                                                    # consider current i as smallest

        # sequently compare numbers to the right of i with i
        for j in range(i + 1, n):
            comparisons += 1
            if numbers[j] < numbers[smallest]:
                smallest = j                                            # if smaller value is found, returns it
        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]   # change i with a smaller j 
    return comparisons