def intersection(arrays):
    # TODO: O(n)?
    array_count = len(arrays)
    result = []
    unique_values = {}
    for array in arrays:

        for value in array:
            if value in unique_values:
                unique_values[value] += 1
            else:                
                unique_values[value] = 1

            if unique_values[value] == array_count:
                result.append(value)
            
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
