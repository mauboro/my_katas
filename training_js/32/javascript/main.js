function roundIt(n){
  string = String(n).split(".");
  if (string[0].length < string[1].length){
    return Math.ceil(n);
  }else if (string[0].length > string[1].length){
    return Math.floor(n);
  }else {
    return Math.round(n);
  }
}
