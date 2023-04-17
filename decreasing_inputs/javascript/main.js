function add(...args){
  let total = 0;
  let count = 1;
  for (let i = 0; i < args.length; i++){
    total += args[i] / count;
    count += 1;
  }
  return Math.round(total);
}
