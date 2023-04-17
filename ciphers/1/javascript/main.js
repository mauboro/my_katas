function encode(text){
  let res = "";
  let alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for (let i = 0; i < text.length; i++){
    if (alphabet.includes(text[i])){
      if (alphabet.indexOf(text[i]) % 2 != 0){
        res += "1";
      }
      else if (alphabet.indexOf(text[i]) % 2 === 0){
        res += "0";
      }
    }
    else if (text[i] === " "){
      res  += " ";
    }
    else {
      res += text[i];
    }
  }
  return res;
}

const encodeRefactored = text => text.replace(/[a-z]/gi, c => 1 - c.charCodeAt(0) % 2);
