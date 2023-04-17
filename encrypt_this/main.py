def encrypt_this(text):
    if not text: return ""
    res = []
    for word in text.split():
        if len(word) >= 3:
            res.append("!" + str(ord(word[0])))
            res.append(word[-1])
            for l in word[2:-1]:
                res.append(l)
            res.append(word[1])
        elif len(word) == 2:
            res.append("!" + str(ord(word[0])))
            res.append(word[-1])
        elif len(word) == 1:
            res.append("!" + str(ord(word)))
        
    
    return (" ".join(("".join(res)).split("!"))).lstrip()



def encrypt_this_beautifully_refactored(text):
    res = []
    
    for word in text.split():
        word = list(word)
        
        word[0] = str(ord(word[0]))
        
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        
        
        res.append("".join(word))
            
   
    return " ".join(res)
