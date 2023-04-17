function changeMe(moneyIn){
  let test = "40p";
  console.log(test.slice(0, -1));
  if (moneyIn.slice(0, 1) === "£") {
    switch (moneyIn.slice(-1)) {
        case "5":
            return ("20p ".repeat(25)).slice(0, -1)
        case "2":
            return ("20p ".repeat(10)).slice(0, -1)
        case "1":
            return ("20p ".repeat(5)).slice(0, -1)
        default:
            return moneyIn;
    }
  }else if (moneyIn.slice(-1) === "p"){
    switch (moneyIn.slice(0, -1)){
        case "50":
            return "20p 20p 10p";
        case "20":
            return "10p 10p";
        case "10":
            return "10p";
        default:
            return moneyIn;
    }
  }else {
    return moneyIn
  }
}
