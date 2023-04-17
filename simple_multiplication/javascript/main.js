function simpleMultiplication(number) {
  if (number % 2 == 0) {
    return number * 8
  } else {
    return number * 9
  }
}

function simpleMultiplicationRefactored(number) {
	return number * (number % 2 ? 9 : 8)
}
