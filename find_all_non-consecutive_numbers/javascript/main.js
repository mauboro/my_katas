function allNonConsecutive (arr) {
  let res = new Array();
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] + 1 !== arr[i + 1]){
        res.push({"i": i+1, "n" :arr[i + 1]});
    }
  }
  for (let i = 0; i <= res.length; i++){
    if (typeof res[i] === "undefined" || typeof res[i].n === "undefined"){
      delete res[i];
    }
  }
  let res2 = res.filter(x => x !== "undefined");
  return res2;
}

function allNonConsecutiveRefactored (arr) {
  let res = [];
  for (let i = 1; i < arr.length; i++){
    if (arr[i] - arr[i - 1] !== 1) res.push({i: i, n: arr[i]})
  }
  return res;
}
