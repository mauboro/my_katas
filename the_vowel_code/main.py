def encode(st):
    return st.translate(st.maketrans("aeiou", "12345"))
    
def decode(st):
    return st.translate(st.maketrans("12345", "aeiou"))
