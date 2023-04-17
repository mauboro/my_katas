def any_arrows(arrows):
    if not arrows: return bool(len(arrows))
    for a in arrows:
        if a.get("damaged", 0) == False:
            return True 
    return False
