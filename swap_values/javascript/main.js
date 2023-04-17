function swapValues() {
    var args = arguments["0"];
    var temp = args[0];
    args[0] = args[1];
    args[1] = temp;
    console.log(args)
}

function swapValues(){
  return arguments[0].reverse();
}
