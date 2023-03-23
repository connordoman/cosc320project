


'''
Store the phrases in a trie, indexed by the first word.
Python dictionaries are hash tables, so accessing the dict is O(1) for the given word of the corpus.
'''

class ReplacementPhrase:
    def __init__(self, phrase, replacement):
        self.phrase_word_pairs = {}
        self.phrase = phrase
        self.current_word = ""
        self.count = 0

        replacements = replacement.split(" ")
        for word in phrase.split(" "): # build the phrase word pairs
            self.phrase_word_pairs[word] = replacements[self.count]
            self.count += 1

        

    def get_current_word(self):
        return self.phrase_words[self.current_word]
    
    def get_next_word(self):
        self.current_word += 1
        return self.phrase_words[self.current_word]
    
    def reset_search(self):
        self.current_word = 0

    def get_size(self):
        return self.count

    def __str__(self):
        return self.phrase + " " + str(self.count)

replacement_keys = {
    "quick": ReplacementPhrase("quick brown", "dang slow"),
    "dog": ReplacementPhrase("dog", "cat"),

}


class PhraseTrie:
    def __init__(self):
        self.root = {}
        self.current_branch = ""
        self.current_word = -1


    

class WordReplacer:
    def __init__(self):
        self.body = ""
        self.words = []
        self.offset = 0
        self.phrases = PhraseTrie()

    def prepare(self, phrases, body):
        self.body = body
        buffer = ""
        # split body into words by space
        for c in body:
            if c == " ":
                self.words.append(buffer)
                buffer = ""
            else:
                buffer += c
        self.words.append(buffer)
            
        self.phrases = PhraseTrie()
        for phrase in phrases:
            self.phrases.add(phrase.split(" "))

    '''
    1. Iterate through the words in the body
    2. If the word is in the trie, then we have a match
    3. If the word is not in the trie, then we do not have a match
    4. If the word is in the trie, add to the offset counter
    5. If the offset counter is equal to the length of the phrase, then we have a full match
    6. If the offset counter is not equal to the length of the phrase, then we do not have a full match
    7. If we have a full match, then replace the phrase with the replacement
        - Replace element (i - offset) of the body with the entire replacement statement
        - Set all other [i - offset + 1 : i] elements of the phrase to ""
        - Use the offset counter to determine how many words to remove from the list
    8. If we do not have a full match, then do not replace the phrase, but we still iterate again

    '''

    def replace_all_occurrences(self):
        for w in self.words: # words in the body
            if self.phrases.word_in_trie(w): # if the word is in the trie
                # we have a match
                if self.offset == self.phrases.get_size(): # if the offset counter is equal to the length of the phrase, then we have a full match
                    # replace the phrase with the replacement
                    self.words[i - self.offset] = self.phrases.get_replacement()
                    for i in range(self.offset):
                        self.words[i - self.offset + 1] = ""

                    
                    self.offset = 0 # reset the offset counter
                    self.phrases.current_word = -1 
                else: # if the offset counter is not equal to the length of the phrase, then we do not have a full match
                    pass
                self.offset += 1 # add to the offset counter
                print("")
            else: # if the word is not in the trie
                print()

    # end of class


def main():
    body = "The quick brown fox jumped over the lazy dog"
    phrase1 = ReplacementPhrase("quick brown", "dang slow")
    phrase2 = ReplacementPhrase("dog", "cat")
    word_replacer = WordReplacer()
    word_replacer.prepare(phrases, body)
    word_replacer.replace_all_occurrences()
    print(word_replacer.words)

if __name__ == "__main__":
    main()