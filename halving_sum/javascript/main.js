function halvingSum(n) {
  if (n == 1){
    return n;
  }
  return n + halvingSum(Math.floor(n/2));
}
