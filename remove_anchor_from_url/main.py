def remove_url_anchor(url):
    return url[:url.index("#")] if  "#" in url else url

def remove_url_anchor_refactored(url):
    return url.split("#")[0]

