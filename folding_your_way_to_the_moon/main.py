def fold(paper):
    return paper * 2

def fold_to(distance):
    if not(distance >= 0): return None
    paper = 0.0001
    folds = 0
    while paper < distance:
        paper = fold(paper)
        folds += 1
    return folds
     
    
        
