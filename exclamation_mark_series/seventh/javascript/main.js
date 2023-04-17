function remove (string) {
  let res = [];
  for (let w of string.split(" ")){
    if (w.split("!").length - 1 != 1){
      res.push(w);
    }
  }
  return res.join(" ");

