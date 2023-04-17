def double_every_other(lst):
    return [l*2 if i % 2  else l for i, l in enumerate(lst)]
