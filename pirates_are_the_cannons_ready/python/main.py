def cannons_ready(gunners):
    if "nay" not in gunners.values():
        return "Fire!"
    else:
        return "Shiver me timbers!"
