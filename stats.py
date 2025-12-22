def word_count(text):
    words = len(text.split())
    print(f"Found {words} total words")

def char_count(text):
    d = {}
    for x in text.lower():
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1
    return d