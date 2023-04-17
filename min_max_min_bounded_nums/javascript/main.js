function minMinMax(array) {
  min = Math.min(...array);
  max = Math.max(...array);
  let mna = 0;
  for (let i = min; i < max; i++){
    if (!array.includes(i)){
      mna = i;
      break;
    }
  }
  return [min, mna, max]
}
