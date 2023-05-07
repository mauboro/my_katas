function arrayMadness(a, b) {
  return a.map(x => x ** 2).reduce((x,y) => x + y) > b.map(x => x ** 3).reduce((x,y) => x + y)
}
