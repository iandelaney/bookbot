from stats import word_count, char_count


def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    return book_text
    #print(book_text)


    
print(word_count(main()))
print(char_count(main()))


# main()
