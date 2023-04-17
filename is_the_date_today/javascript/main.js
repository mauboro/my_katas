function isToday(date) {
  let d = new Date();
  return date.getDate() === d.getDate() && date.getDay() === d.getDay();
}
