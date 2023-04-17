function solve(s){
  if (s.length === 0) {
    return [0, 0, 0, 0]
  }
  let up = 0, lo = 0, n = 0, sp = 0;
  for (let i = 0; i <= s.length; i++){
      if (/[A-Z]/.test(s[i])){
        up += 1
      }else if (/[a-z]/.test(s[i])){
        lo += 1;
      }else if (/^\d$/.test(s[i])){
        n += 1;
      }else{
        sp += 1;
      }
  }
  return [up, lo - 1, n, sp];
}
