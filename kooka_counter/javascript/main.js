var kookaCounter = function(laughing) {
  let diff = "";
  let count = 0;
  for (let c of laughing){
    if (c === "h" && diff != "h"){
      count += 1;
      diff = "h";
    }
    if (c === "H" && diff != "H"){
      count += 1;
      diff = "H";
    }
  }
  return count;
}

var kookaCounterRefactored = function(laughing){
	return (laughing.match(/(Ha)+|(ha)+/g) || []).length;
}
