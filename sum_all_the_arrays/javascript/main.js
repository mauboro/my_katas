function arraySum(arr) {
  res = 0;
  for (let a of arr){
    if (typeof a === "object"){
      res += arraySum(a);
    }else if (typeof a == "number"){
      res += a;
    }
  }
  return res;
}

