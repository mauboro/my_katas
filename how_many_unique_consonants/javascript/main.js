function countConsonants(str) {
  let res = [];
  consonants = "bcdfghjklmnpqrstvwxyz"
  for (s of str){
    if (consonants.includes(s.toLowerCase()) && !(res.includes(s.toLowerCase()))){
      res.push(s.toLowerCase())
    }
  }
  return res.length;
}

function countConsonantsRefactored(str) {
	return Set(str.toLowerCase().replace(/[^a-z]|[aeiou]/g, "")).size
}
