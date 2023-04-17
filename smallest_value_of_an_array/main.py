def find_smallest(arr,to_return):
    return  min(arr) if to_return == "value" else arr.index(min(arr))
