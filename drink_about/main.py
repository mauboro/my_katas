def people_with_age_drink(age):
    beverage = ""
    if age < 14:
        beverage =  "toddy"
    elif age < 18:
        beverage =  "coke"
    elif age < 21:
        beverage =  "beer"
    elif age >= 21:
        beverage =  "whisky"
    
    return f"drink {beverage}"

def people_with_age_drink_refactored(age):
    if age > 20: return "drink whisky"
    if age > 17: return "drink beer"
    if age > 13: return "drink coke"

    return "drink toddy"
