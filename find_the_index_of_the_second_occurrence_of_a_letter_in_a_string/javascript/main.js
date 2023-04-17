function secondSymbols(s, symbol){
	if (!s.includes(symbol)){
		return -1;
	}
	let count = 0
	for (let i = 0; i < s.length; i++){
		if (count == 2){
			return i;
		}
		if (s[i] === symbol){
			count += 1;
		}
	}
	return -1
}
