def make_backronym(acronym):
    return " ".join([dictionary[a.upper()] for a in acronym])
