
REPLACEMENT_DICTIONARY = {
    "the": "THE",
}

def replace_with_new_word(text):
    text = text.strip()

    # splitting the words in T
    text_array = []
    buffer_word = ""
    for char in text:
        
        if char == " ":
            text_array.append(buffer_word)
            buffer_word = ""
        else:
            buffer_word += char
    text_array.append(buffer_word)

    # replacing the words in T
    for old_word, replacement in REPLACEMENT_DICTIONARY.items():
        for word in text_array:
            if word == old_word:
                text_array[text_array.index(word)] = replacement
    
    # rebuilding the string
    text = ""
    for word in text_array:
        text += word + " "

    return text

def main():
    text = "the quick brown fox jumps over the lazy dog"
    print("\n" + replace_with_new_word(text) + "\n")

if __name__ == "__main__":
    main()