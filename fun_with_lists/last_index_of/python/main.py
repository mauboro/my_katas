def last_index_of(head, val):
    c = 0
    f = 0
    i = 0
    while head:
        if head.data == val:
            i = c
            f = 1
        c += 1
        head = head.next
    return i if f else -1

def last_index_of_refactored(head, val):
    c = 0
    i = -1
    while head:
        if head.data == val:
            i = c
        c += 1
        head = head.next
    return i 
