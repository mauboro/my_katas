function sumOfDifferences(arr) {
  if (arr.length != 0){
    return Math.max(...arr) - Math.min(...arr);
  }
  else{
    return 0;
  }
}

function sumOfDifferencesRefactored(arr) {
	return  arr.length > 1 ? Math.max(...arr) - Math.min(...arr) : 0;
}
