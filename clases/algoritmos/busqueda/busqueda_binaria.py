def binary_search(order_list:list, search_value:int):
    first = 0
    last = len(order_list) - 1

    while first <= last:
        middle = (first + last) // 2
        if search_value == order_list[middle]:
            return True
        elif search_value < order_list[middle]:
            last = middle - 1
        else:
            first = middle + 1
    
    return False
    
order_list = [2,5,8,12,16,23,38,56,72,91]
print(binary_search(order_list, 2))