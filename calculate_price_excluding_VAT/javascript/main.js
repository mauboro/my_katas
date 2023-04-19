function excludingVatPrice(price){
  if (price === 0){
    return 0;
  }
  if (!price){
    return -1;
  }
  return Number((price/1.15).toFixed(2));
}
