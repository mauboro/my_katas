function calculator(a,b,sign){
  if (!("+-*/").includes(sign)) {
    return "unknown value";
  }
    if (sign == "+") {
      return a + b;
    } else if (sign == "-") {
      return a - b;
    } else if (sign == "*") {
      return a * b;
    } else if (sign == "/") {
      return a / b;
    }
}

function calculatorRefactored(a,b,sign){
  if ((typeof a === "number") && (typeof b === "number")){
    switch (sign){
        case "+":
            return a + b;
        case "-":
            return a - b;
        case "/":
            return a / b;
        case "*":
            return a * b;
        default:
            return "unknown value";
    }
  }
}
