from string import ascii_lowercase as s

def words_to_marks(string):
    dicto = {l: i + 1 for i, l in enumerate(s)}
    return sum([dicto[l] for l in string])
