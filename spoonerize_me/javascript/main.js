function spoonerize(words) {
  let w = words.split(" ");
  return w[1][0] + w[0].slice(1) + " " + w[0][0] + w[1].slice(1);
}
