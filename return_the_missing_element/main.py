def get_missing_element(seq): 
    for i in range(10):
        if str(i) not in [str(s) for s in seq]:
            return int(i)

#that's too much for me bruh wtf
def get_missing_element_refactored(seq):
    return 45 - sum(seq)
