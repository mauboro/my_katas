function logicalCalc(array, op){
  operators = {"AND": "&&", "OR": "||", "XOR": "^"}
  return !!array.reduce((a , b) => (eval(`${a} ${operators[op]} ${b}`)))
}
