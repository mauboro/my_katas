def alphabet_war(fight):
    dicto = {
        "w": 4,
        "m": 4,
        "p": 3,
        "q": 3,
        "d": 2,
        "b": 2,
        "s": 1,
        "z": 1,
    }
    left_side = 0
    right_side = 0
    for l in [c for c in fight]:
        if l in "wpbs":
            left_side += dicto[l]
        elif l in "mqdz":
            right_side += dicto[l]
    return "Right side wins!" if right_side > left_side else "Left side wins!" if left_side > right_side else "Let's fight again!"

def alphabet_war_refactored(fight):
    d = {'w':4, 'p':3, 'b':2,'s':1, 'm':-4, 'q':-3, 'd':-2, 'z':-1}
    res = sum([d[c] for c in fight if c in d])
    
    return {
        res==0: "Let's fight again!",
        res>0: "Left side wins!",
        res<0: "Right side wins!"
    }[True]
