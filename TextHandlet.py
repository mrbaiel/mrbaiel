class TextHandler:
    def __init__(self):
        self.words = ''
        self.short_words = ''
        self.long_words = []

    def add_words(self, word_list):
        self.words + (word_list)

    def get_shortest_words(self):
        min_len = min([len(i) for i in self.words])
        for i in list(self.words):
            if i == min_len:
                self.short_words.append(i)
            else: continue
        return self.short_words
            
