def correct_polish_letters(st): 
    dicto = { 'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z' }
    return "".join(dicto[s] if s in dicto else s for s in st)
    z', 'ż':'z' }
