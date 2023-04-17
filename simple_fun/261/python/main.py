def whoseMove(lp, win):
    if win:
        if lp == "white":
            return lp
        else:
            return "black"
    elif not win:
        if lp == "white":
            return "black"
        else:
            return "white"
