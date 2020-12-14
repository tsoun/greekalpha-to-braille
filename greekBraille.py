class text:
    def __init__(self, lexicon):
        self.greekAlpha = []
        self.greekBraille = []
        self.lexicon = lexicon

    def read(self):
        self.greekAlpha = input()

    def transcribe(self):
        for letter in self.greekAlpha:
            try:  # TODO: EVERYTHING
                self.greekBraille.append(self.lexicon[letter])
            except:
                self.greekBraille.append(letter)
        self.greekBraille = "".join(self.greekBraille)
        self.greekAlpha = "".join(self.greekAlpha)

    def printLexicon(self):
        print(self.lexicon)


def main():
    lexicon = readLexicon()
    TEXT = text(lexicon)
    TEXT.read()
    TEXT.transcribe()
    print(TEXT.greekBraille)


def readLexicon():
    d = {}
    with open("lexicon.txt", encoding="utf-8") as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
    return d


main()
