class Class():
    def __init__(self, text):
        self.ParseText(text)

    def ParseText(self,text):
        self.day = text[:text.find(" -")]
        text = text[text.find("- ") + 2:]

        self.start = text[:text.find(" -")]
        self.end = text[text.find("- ") + 2:]
