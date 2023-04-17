function sumEvenNumbers(inp) {
  let res = 0;
  for (let i = 0; i <= inp.length;i++){
    if (inp[i] % 2 == 0){
      res += inp[i];
    }
  }
  return res;
}

