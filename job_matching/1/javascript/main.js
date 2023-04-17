function match(c, j) {
  if (!c.minSalary || !j.maxSalary){
    throw Error;
  }
  if ((c.minSalary * 0.9) <= j.maxSalary){
    return true;
  }
  return false;
}
