function findMultiples(integer, limit) {
  const arr = [];
  for (let i = integer; i <= limit; i += integer){
    arr.push(i);
  }
  return arr;
}
