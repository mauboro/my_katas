function dutyFree(normPrice, discount, hol){
  return Math.trunc(hol / ((discount/100) * normPrice ));
}
