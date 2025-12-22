import sys

from stats import word_count, char_count, sort_char_count   

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    return book_text
    #print(book_text)
    
# print(word_count(main()))
# print(char_count(main()))
# main()
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#print pretty report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_count(main())} total words")
print("--------- Character Count -------")

my_dict = (sort_char_count(char_count(main())))

for k, v in my_dict.items():
	print (k+':', v)
     
print("=================================")