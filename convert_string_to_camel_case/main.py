def to_camel_case(text):
    if not text: return ""
    new_text = text.replace("_", "-")
    return "".join([word.capitalize() if idx != 0 else word for idx, word in enumerate(new_text.split("-"))])
