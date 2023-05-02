function one(arr, fun){
  if (arr.filter(x => fun(x) === true).length === 1){
    return true;
  }else {
    return false;
  }
}

const oneRefactored = (arr, fun) =>  arr.filter(fun).length === 1;
