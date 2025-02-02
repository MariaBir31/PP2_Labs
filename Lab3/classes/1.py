class Stringsss():
    def __init__(self, text):
        self.text = text

    def getString(self):
        print(self.text)

    def printString(self):
        print(self.text.upper())


m = Stringsss("Hello")
t = "Hello"

m.getString()
m.printString()