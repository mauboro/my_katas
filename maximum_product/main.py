def adjacent_element_product(array):
    return max(list(map(lambda a, b: a * b, array, array[1:])))
    

