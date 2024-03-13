class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        words = [w.lower() for w in words]
        return [w for w in words if sorted(w) == sorted(self.word) and w != self.word]