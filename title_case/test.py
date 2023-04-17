def title_case_refactored(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()

    return " ".join([word if word in minor_words else word.capitalize() for word in title])

a = "THE WIND IN THE WILLOWS"
print(a.capitalize())
print(a.title())


