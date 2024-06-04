def main():
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    n_words = words_count(text)
    n_chars = chars_count(text)
    n_chars = convert_dict(n_chars)
    n_chars.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{n_words} found in the document")
    for char in n_chars:
        print(f"The \'{char['name']}\' character was found {char['num']} times")
    print("--- End report ---")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def words_count(book):
    return len(book.split())

def chars_count(book):
    chars = set(book.lower())
    chars_dic = {char: book.count(char) for char in chars if char.isalpha()}
    return chars_dic

def convert_dict(dict):
    listdict = []
    for k in dict:
        listdict.append({"name": k, "num": dict[k]})
    return listdict

def sort_on(dict):
    return dict["num"]

main()