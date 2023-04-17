def fly_by(lamps, drone):
    if len(drone) > len(lamps):
        drone = drone[1:]
    return "o" * len(drone) + "x" * (len(lamps) - len(drone))

def fly_by_refactored(lamps, drone):
    return lamps.replace("x", "o", len(drone))
