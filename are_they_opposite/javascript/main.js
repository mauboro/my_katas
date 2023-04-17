function swapcase(str) {
  let result = '';
  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (char === char.toUpperCase()) {
      result += char.toLowerCase();
    } else if (char === char.toLowerCase()) {
      result += char.toUpperCase();
    } else {
      result += char;
    }
  }
  return result;
}

function isOpposite(s1,s2){
  if (s1.length === 0 || s2.length === 0){
    return false;
  }
  let swapped = swapcase(s1);
  return swapped === s2;
  
