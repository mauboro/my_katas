var isSquare = function(arr){
  if (!arr.length) return undefined;
  return arr.every(x => Math.sqrt(x) == Math.round(Math.sqrt(x))); 
}

