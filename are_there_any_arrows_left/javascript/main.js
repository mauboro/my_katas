function anyArrows(arrows){
  if ((arrows.some(x => x.range)) && (arrows.length > 2)) return true;
  return arrows.some(x => x.damaged === false);
}

const anyArrowsRefactored = arrows => arrows.some(x => !x.damaged);
