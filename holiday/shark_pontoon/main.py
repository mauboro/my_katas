def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin: 
        shark_speed *= 0.5
    while True:
        shark_distance -= shark_speed
        if shark_distance <= 0:
            return "Shark Bait!"
        pontoon_distance -= you_speed  
        if pontoon_distance <= 0:
            return "Alive!"


def shark_refactored(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2
        
    shark_eat_time = shark_distance / shark_speed
    you_safe_time = pontoon_distance / you_speed
    
    return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"

