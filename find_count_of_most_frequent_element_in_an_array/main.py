def most_frequent_item_count(collection):
    if not collection: return 0
    return max(collection.count(c) for c in collection)
