function sc(apple){
  res = [];
  for (let i = 0; i < apple.length; i++){
    if (apple[i].indexOf("B") != -1){
      res.push(i, apple[i].indexOf("B"));
    }
  }
  return res;
}
