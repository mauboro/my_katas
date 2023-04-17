function whoseMove(lastPlayer, win) {
  if (win === true){
    if (lastPlayer === "white"){
      return "white";
    }else{
      return "black";
    }
  }else if (win === false){
    if (lastPlayer === "white"){
      return "black";
    }else {
      return "white";
    }
  }
}

function whoseMove(lastPlayer, win){
	return win ? lastPlayer:lastPlayer==="white" ? "black":"white";
}
