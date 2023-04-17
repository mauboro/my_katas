def get_strings(city):
    return ",".join([f"{l}:{'*' * city.lower().count(l)}" for l in sorted(set(city.lower()), key=city.lower().index) if l != " "])


