function vowelOne(s){
  let letters = "aeiouAEIOU";
  let res = ""
  for (let i = 0;i < s.length;i++){
    if (letters.includes(s[i])){
      res += "1";
    }else{
      res += "0";
    }
  }
  return res;
}
