def even_numbers(arr,n):
    result = []
    for a in arr[::-1]:
        if len(result) < n:
            if a % 2 == 0:
                result.append(a)
        else:
            break
    return result[::-1]


def even_numbers_refactored(arr,n):
    return [a for a in arr if a % 2 == 0][-n:]
