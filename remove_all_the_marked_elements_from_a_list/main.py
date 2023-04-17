class List:
    def remove_(self, integer_list, values_list):
        for _ in range(4):
            for n in integer_list:
                if n in values_list:
                    integer_list.remove(n)
        return (integer_list)

class List:
    def remove_obviously_refactored(self, integers, values):
        return [n for n in integers if n not in values]
