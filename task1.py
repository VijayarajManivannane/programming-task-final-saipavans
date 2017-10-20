book_list = ["Book1.txt", "Book2.txt", "Book3.txt"]

def main():
    largest_word = ""
    for book in book_list:
        fin = open(book)
        for line in fin:
            line_stripped = line.strip()
            line_words = line_stripped.split()
            for word in line_words:
                if len(word) > len(largest_word):
                    largest_word = word
        fin.close()
    print("Largest word is : ", largest_word)

if __name__ == '__main__':
    main()