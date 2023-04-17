def crap(garden, bags, cap):
    for part in garden:
        if "D" in part:
            return "Dog!!"
    shit_in_the_garden = sum([part.count("@") for part in garden])
    if bags * cap >= shit_in_the_garden:
        return "Clean"
    else:
        return "Cr@p"
