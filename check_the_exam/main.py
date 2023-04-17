def check_exam(arr1,arr2):
    total = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            total += 4
        elif arr2[i] == "":
            total += 0
        else: 
            total -= 1
    
    return total if total > 0 else 0


def check_exam_refactored(arr1,arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))
  

#the zip function returns a iterator of tuples, where the i-th tuple contains the i-th element from each sequence or iterables passed in as arguments
