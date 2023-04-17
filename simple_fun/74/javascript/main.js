function growingPlant(up, down, desiredHeight) {
  let total = 0;
  let days = 0;
  while (total < desiredHeight){
    total += up;
    if (total >= desiredHeight){
      days += 1;
      break;
    }
    total -= down;
    days += 1;
  }
  return days;
}
