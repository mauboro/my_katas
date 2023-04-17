function bonusTime(salary, bonus) {
  if (bonus){
    return `£${salary * 10}`;
  }
  else{
    return `£${salary}`;
  }
}

const bonusTimeRefactored = (salary, bonus) => `£${salary * (bonus ? 10:1)}`;



