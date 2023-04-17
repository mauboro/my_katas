def meeting(rooms):
    for i, r in enumerate(rooms):
        if r == "O":
            return i
    return "None available!"

