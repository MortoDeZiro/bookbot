def main():
    with open("books/Frankenstein.txt") as opened_book:
        word_count = 0
        tupled_words = ()
        char_dict = {}
        lowered_chars = ""
        file_contents = opened_book.read()
        tupled_words = file_contents.split()
        word_count = len(tupled_words)
        print(f"The book has {word_count} words.")

        lowered_chars = file_contents.lower()

        for char in lowered_chars:
            if char not in char_dict:
                char_dict[char] = 0
            else:
                char_dict[char] += 1
        
        for key, value in char_dict.items():
            if key != "\n":
                print(f"The {key} character was found {value} times")


        

if __name__ == "__main__":
    main()