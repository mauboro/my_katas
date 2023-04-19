function convertHashToArray(hash){
  let res = [];
  for (let k of Object.keys(hash)){
    res.push([k, hash[k]]);
  }
  return res.sort();
}

const convertHashToArrayRefactored = h => Object.entries(h).sort()

