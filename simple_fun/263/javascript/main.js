function evenNumbersBeforeFixed(array, fixedElement) {
  let count = 0;
  if (!array.includes(fixedElement)){
    return -1
  }
  for (let n of array){
    if (n === fixedElement){
      break;
    }else if (n % 2 == 0){
      count += 1;
    }
  }
  return count;
}
