def word_count(text):
    words = len(text.split())
    #print(f"Found {words} total words")
    return words

def char_count(text):
    d = {}
    for x in text.lower():
        if x.isalpha():
            if x in d:
                d[x] = d[x] + 1
            else:
                d[x] = 1
    return d

def sort_char_count(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

