function keepOrder(ary, val) {
  ary.push(val);
  return ary.sort().indexOf(val);
}

function keepOrderRefactored(ary, val){
	console.log(ary.filter(a >= a < val))
}

let keepOrderRefactoredAgain = require("lodash").sortedIndex

