#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    f = open(fileName)
    longest = ""

    for line in f:
        if len(line) > 0 and line[-1] == "\n":
            line = line[:-1]

        if len(line) > len(longest):
            longest = line

    f.close()
    return longest


def toBinary(fileName):
    f = open(fileName)
    text = ""

    for line in f:
        if len(line) > 0 and line[-1] == "\n":
            line = line[:-1]

        text += line
    f.close()
    out = []
    for i in range(0, len(text), 8):
        out.append(text[i:i+8])

    return out