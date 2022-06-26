from sys import *

vars = {}

def open_file(filename):
    data = open(filename, "r").read()
    data = data.replace('\n', '')
    data = data.split(';')
    data = data[:-1]
    return data

def parse(filecontents):
    for i in filecontents:
        if i[0:5] == "print":
            text = i.replace("print", '')
            quotes = []
            spaces = []
            for j in range(len(text)):
                if text[j] == "\"":
                    quotes.append(j)
                if text[j] == " ":
                    spaces.append(j)
        elif i[0:3] == "let":
            let = i.replace("let", "")
            firstquote = let.index("\"")
            
            let = let.replace(" ", "")
            equals = 0
            for j in range(len(let)):
                if let[j] == "=":
                    equals = j

            lets[let[0:equals]] = let[equals+1:].replace("\"", "")

            print(text[quotes[0] + 1:quotes[1]])

            
def run():
    data = open_file(argv[1])
    parse(data)

run()

