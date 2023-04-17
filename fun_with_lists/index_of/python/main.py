def index_of(head, value): 
    if not head: return -1
    if value == head.data: return 0
    current = head
    count = 0
    while current.next:
        if value == current.data:
            return count
        else:
            current = current.next
            count += 1
   return -1

def index_of_refactored(head, value): 
i = 0
while head and head.data != value:
    head = head.next
    i += 1
return i if head else -1

