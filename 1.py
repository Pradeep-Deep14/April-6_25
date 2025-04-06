def string_stats(text):
    length = len(text)
    unique_chars = len(set(text))
    first_char = text[0]
    upper_count = 0  # Initialize upper_count

    for char in text:
        if char.isupper():
            upper_count += 1

    stats = {
        "length": length,
        "unique": unique_chars,
        "first": first_char,
        "upper": upper_count,
    }

    return stats

result = string_stats("Hello World")
print(result)