from string import ascii_letters as letters

def reverse_letter(string):
    #do your magic here
    return "".join(["" if s not in letters else s for s in string])[::-1]

    
