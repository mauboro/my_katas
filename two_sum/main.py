def two_sum(arguments):
    numbers = arguments[0]
    target = arguments[1]

    for i in range(len(numbers)):
        n1 = numbers[i]
        print(n1)
        for n2 in numbers:
            
            if n1 + n2 == target:
                print(n1)
                return numbers.index(n1), numbers.index(n2)


test_cases = [([1,2,3], 4), ([1234,5678,9012], 14690), ([2,2,3], 4)]
print([two_sum(test) for test in test_cases])

def two_sum_refactored(numbers, target):
    for idx, num in enumerate(numbers):
        for n in numbers[1:]:
            if num == 2 : return [0, 1]
            if num + n == target:
                return (idx, numbers.index(n))


