function reverseList(arr) {
  let res = [];
  for (let i = arr.length - 1; i >= 0; i--){
    console.log(i);
    res.push(arr[i]);
  }
  return res;
}
