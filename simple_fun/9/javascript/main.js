function arrayPacking(a) {
  a = a.reverse();
  let res = "";
  for (let i = 0; i < a.length; i++){
    res += (a[i].toString(2).padStart(8, "0"));
  }
  return parseInt(res, 2);
}
