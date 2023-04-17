def stock_list(list_of_art, list_of_cat):
    book_pairs = []
    cap_pairs = []
    for book in list_of_art:
        book_pairs.append((book[0], int(book.split()[1])))
    for cap in list_of_cat:
        cap_pairs.append([cap, 0])
    
    for cap in cap_pairs:
        for book in book_pairs:
            if cap[0] == book[0]:
                cap[1] += book[1]
                           
    if not list_of_art: return ""
    return " - ".join([f"({cap[0]} : {cap[1]})" for cap in cap_pairs])
    
