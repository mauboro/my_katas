function all( arr, fun ){
  for (let i = 0; i < arr.length; i++){
    if (!(fun(arr[i]))){
      return false;
    }
  }
  return true;
}

const allRefactored = (arr, fun) => arr.every(fun);
