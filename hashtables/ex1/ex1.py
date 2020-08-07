def get_indices_of_item_weights(weights, length, limit):
    d = {}    
    for index, num in enumerate(weights):
        d[num] = index

    for index, weight in enumerate(weights):
        target = limit - weight
        if target in d:
            next_index = d[target]

            if index > next_index:
                first = index
                second = next_index
            else:
                first = next_index
                second = index

            return (first, second)
    return None

    # O(n^2):

    # for index, weight in enumerate(weights):
    #     for next_index, next_weight in enumerate(weights):
    #         if index != next_index:
    #             if index > next_index:
    #                 first = index
    #                 second = next_index
    #             else:
    #                 first = next_index
    #                 second = index

    #             weight_dict[weight+next_weight] = (first, second)
    # try:
    #     return weight_dict[limit]
    # except:
    #     return None

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

print(answer_2)