def band_name_generator(name):
    return (name[:-1] + name).capitalize() if name[0] == name[-1] else f"The {name.capitalize()}"
