function divisibleBy(numbers, d){
  let res = [];
  for (let i = 0; i < numbers.length; i++){
    if (numbers[i] % d === 0 ){
      res.push(numbers[i]);
    }
  }
  return res;
}

const divisibleByRefactored = (numbers, divisor) => numbers.filter(n => n % divisor === 0);
