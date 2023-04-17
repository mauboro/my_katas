function firstNonRepeated(str) {
  let s = str.split("");
  for (let i = 0; i <= s.length; i++){
    if ((s.filter(x => x == s[i]).length == 1)){
      return s[i];
    }
  }
  return null;
}

const firstNonRepeatedRefactored = s => [...s].find(s.indexOf(i) == s.lastIndexOf(i)) || null
