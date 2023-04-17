function sumNoDuplicates(numList) {
  let res = 0;
  for (let n of numList){
    if ((numList.filter(x => x === n)).length === 1){
      res += n;
    }
  }
  return res;
}
