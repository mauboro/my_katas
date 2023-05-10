function howManyDalmatians(n){
  var dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIANS!!!"];
  
  if (n <= 10){
    return dogs[0];
  } else if (n <= 50){
    return dogs[1];
  } else if (n == 101){
    return dogs[3];
  }else {
    return dogs[2];
  }
}
