class WordCounter:

    def __init__(self, sentence):
        self.sentence = sentence
        self.__wordCount = 0

    def count_words(self):
        list = self.sentence.split(" ")
        self.__wordCount = len(list)

    def get_word_count(self):
        return self.__wordCount

    def get_shortest_word(self):
        list = self.sentence.split(" ")
        min = len(list[0])
        for i in list:
            if len(i) < min:
                min = len(i)
        return min
    
    def get_longest_word(self):
        max = 0
        list = self.sentence.split(" ")

        for i in list:
            if len(i) > max:
                max = len(i)
        return max
            


