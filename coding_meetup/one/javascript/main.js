function countDevelopers(list) {
  let res = 0;
  for (let l of list){
    if (l.language == "JavaScript" && l.continent == "Europe"){
      res += 1;
    }
  }
  return res;
}

const countDevelopersRefactored = (list) => list.filter(x => x.language==="JavaScript" && x.continent === "Europe").length;
