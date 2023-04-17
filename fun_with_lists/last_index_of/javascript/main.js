function lastIndexOf(head, value) {
  let c = 0;
  let i = -1;
  while (head){
    if (head.data === value){
      i = c;
    }
    c += 1;
    head = head.next;
  }
  return i;
}
