function length(head) {
  let c = 0;
  while (head){
    head = head.next
    c += 1;
  }
  return c;
}
