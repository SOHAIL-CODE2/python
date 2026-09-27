def linear_search(arr, target):
    comparisons = 0

    for index in range(len(arr)):
        comparisons += 1

        if arr[index] == target:
            return index, comparisons

    return -1, comparisons


def binary_search_first(arr, target):
    low = 0
    high = len(arr) - 1
    answer = -1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            answer = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return answer, comparisons


def is_sorted_array(arr):
    for index in range(1, len(arr)):
        if arr[index] < arr[index - 1]:
            return False

    return True


def format_array(arr):
    return " ".join(map(str, arr))


def compare_linear_binary_search(arr, target):
    linear_index, linear_comparisons = linear_search(arr, target)

    sorted_status = is_sorted_array(arr)

    sorted_data = sorted(arr)
    sorted_binary_index, sorted_binary_comparisons = binary_search_first(
        sorted_data,
        target
    )

    result = []

    result.append("Search Comparison Report")
    result.append("Original Array: " + format_array(arr))
    result.append("Target: " + str(target))

    result.append("Linear Search on Original")
    result.append("Index: " + str(linear_index))
    result.append("Comparisons: " + str(linear_comparisons))

    if sorted_status:
        result.append("Original Array Sorted: Yes")

        original_binary_index, original_binary_comparisons = binary_search_first(
            arr,
            target
        )

        result.append("Binary Search on Original")
        result.append("Index: " + str(original_binary_index))
        result.append("Comparisons: " + str(original_binary_comparisons))
    else:
        result.append("Original Array Sorted: No")
        result.append("Binary Search on Original")
        result.append("Status: Not Applied")
        result.append("Reason: Binary Search requires sorted data")

    result.append("Sorted Data for Binary Search: " + format_array(sorted_data))
    result.append("Binary Search on Sorted Data")
    result.append("Index: " + str(sorted_binary_index))
    result.append("Comparisons: " + str(sorted_binary_comparisons))
    result.append("Observation: Binary Search is valid only on sorted data")

    return result

arr=[512,442,122,331,112,212]
target=442
print(linear_search(arr,target))
print(binary_search_first(arr , target))
