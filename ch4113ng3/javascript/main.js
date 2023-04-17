function nerdify(txt){
  let res = "";
  for (let i = 0; i < txt.length; i++){
    if (txt[i] === "a" || txt[i] === "A"){
      res += "4";
    }
    else if (txt[i] === "E" || txt[i] === "e"){
      res += "3";
    }
    else if (txt[i] === "l"){ 
      res += "1";
    }
    else{
      res += txt[i];
    }
  }
  return res;
}

const nerdify = t => t.replace(/[aelAE]/g, a => ({'a': 4, "e": 3, "l": 0}[a.toLowerCase()]));
