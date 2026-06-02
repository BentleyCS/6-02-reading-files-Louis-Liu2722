from CSP_6_02_reading_files import toString, longestLine, toBinary

def test_toString():
    f = open("ExampleText.txt", "w")
    f.write("Here is the text\ni am another line")
    f.close()

    assert toString("ExampleText.txt") == "Here is the text\ni am another line"


def test_longestLine():
    f = open("ExampleText.txt", "w")
    f.write("Here is the text\ni am another line")
    f.close()

    assert longestLine("ExampleText.txt") == "i am another line"


def test_toBinary():
    f = open("BinaryText.txt", "w")
    f.write("01101001001010101010")
    f.close()

    assert toBinary("BinaryText.txt") == ["01101001", "00101010", "1010"]