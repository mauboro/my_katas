function sumFactorial(arr){
  function factorial(n){
    if (n === 1){
      return n;
    }
    return n * factorial(n-1);
  }
  return arr.map(x => factorial(x)).reduce((x, y) => x + y);
}
