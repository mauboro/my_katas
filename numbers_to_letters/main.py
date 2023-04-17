from string import ascii_lowercase 

def switcher(arr):
    letters = {l: i for l, i in enumerate(ascii_lowercase[::-1], 1)}
    print(letters)
    letters.update({27: "!", 28: "?", 29: " "})
    print(letters)
    return "".join([letters[int(a)] for a in arr])
    
