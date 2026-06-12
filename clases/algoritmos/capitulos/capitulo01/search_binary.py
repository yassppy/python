def search_binary(order_list: list, search_value: int):
    first = 0
    last = len(order_list) - 1  # len cuenta desde 1 pero los indices son desde 0

    while first <= last:
        middle = (first + last) // 2
        if search_value == order_list[middle]:
            return True
        elif search_value < order_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
        return False


order_list = [1, 2, 3, 4, 6, 7]
search_value = 3
print(search_binary(order_list, search_value))
