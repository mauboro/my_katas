def count_if(head, func):
    c = 0 
    while head:
        if func(head.data):
            c += 1
        head = head.next
    return c 
