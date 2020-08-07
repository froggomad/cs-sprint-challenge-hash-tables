def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}
    #TODO: O(1)
    for index, weight in enumerate(weights):
        for next_index, next_weight in enumerate(weights):
            if index != next_index:
                if index > next_index:
                    first = index
                    second = next_index
                else:
                    first = next_index
                    second = index

                weight_dict[weight+next_weight] = (first, second)
    try:
        return weight_dict[limit]
    except:
        return None

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

print(answer_4)