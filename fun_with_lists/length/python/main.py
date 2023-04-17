def length(head): 
    c = 0
    while head:
        head = head.next 
        c += 1
    return c
