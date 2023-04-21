function stringy(size) {
  let res = "";
  let shift = 1;
  for (let i = 0; i < size; i ++){
    if (shift == 1){
      res += "1";
      shift = 0;
    }else if (shift == 0){
      res += "0"
      shift = 1;
     }
  }
  return res;
}
