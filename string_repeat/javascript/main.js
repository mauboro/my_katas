function repeatStr (n, s) {
	let res = "";
	for (let i = 0;i < n;i++){
		res += s;
	}
	return res;
}

function repeatStrRefactored (n, s){
	return s.repeat(n);
}
