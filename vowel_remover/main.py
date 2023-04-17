def shortcut(s):
   return "".join(["" if c in "aeiou" else c for c in s]) 
