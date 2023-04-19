function twoDecimalPlaces(number) {
  str = (String(number).split("."))
  return Number(str[0] + "." + str[1].slice(0, 2))
}

function twoDecimalPlacesRefactored(number){
	return Math.trunc(number * 100)/100
}
