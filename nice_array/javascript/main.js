function isNice(arr){
  for (let i = 0; i < arr.length; i++){
    if (!(arr.includes(arr[i] + 1)) && !(arr.includes(arr[i] - 1))){
      console.log(arr[i]);
      console.log(arr);
      return false;
    }
  }
  return arr.length > 0;
}

function isNiceRefactored(arr){
	return !!arr.length && arr.every(x => arr.some(y => y + 1 === x || y - 1 === x));
}
