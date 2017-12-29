# Python 2.7.1
# Functions for generating Huffman codewords and Huffman code for ASCII text files
import math

# Returns the counts of symbols in the text file and the length of the file (number of characters).
def frequencies(file):
    frequencies = {}
    f = open(file, 'r')
    length = 0
    for line in f:
        length = length + line.__len__()
        for symbol in line:
            if frequencies.has_key(symbol):
                frequencies[symbol] = frequencies[symbol] + 1
            else:
                frequencies[symbol] = 1
    f.close()
    return frequencies, length


# Returns Huffman codewords for given counts. Input is symbol counts or frequencies in a dictionary and
# length of the text.
def huffman_codewords(freq, length):
    assert isinstance(freq, dict)
    assert isinstance(length, int)
    codewords = {}
    classes = []
    for symbol in freq:
        codewords[symbol] = ""
        classes.append({symbol: freq[symbol]})
    if classes.__len__() == 1:
        symbol = classes[0]
        symbol = symbol.keys()[0]
        codewords[symbol] = "0"
    while classes.__len__() > 1:
        min1 = length
        symbol1 = ''
        min2 = length
        symbol2 = ''
#       Find the class of symbols with the smallest frequency
        for a in classes:
            x = a.values()[0]
            y = a.keys()[0]
            if min1 > x:
                min1 = x
                symbol1 = y
#       Find the class of symbols with second smallest frequency
        for a in classes:
            x = a.values()[0]
            y = a.keys()[0]
            if (min2 > x) & (not symbol1 == y):
                min2 = x
                symbol2 = y
        for symbol in symbol1:
            codewords[symbol] = "0" + codewords[symbol]
        for symbol in symbol2:
            codewords[symbol] = "1" + codewords[symbol]
        newstring = symbol1 + symbol2
        newfreq = min1 + min2
        classes.append({newstring: newfreq})
        classes.remove({symbol1: min1})
#        print(str({symbol2: min2}) + " " + str({symbol1: min1}))
        classes.remove({symbol2: min2})
    return codewords


# Computes the Huffman codewords of a given text and writes the code in a code file.
# Prints the codewords in a dictionary. Prints the average code length and the empirical entropy of the text.
def encode_file(sourcefile, codefile):
    freq, length = frequencies(sourcefile)
    codewords = huffman_codewords(freq, length)
    f1 = open(sourcefile, 'r')
    f2 = open(codefile, 'w')
    for line in f1:
        for symbol in line:
            f2.write(codewords[symbol])
        f2.write("\n") #newline for convenience of reading
    f1.close()
    f2.close()
    print(codewords)
    average_length = 0.0
    empirical_entropy = 0.0
    x = float("inf")
    for s, c in codewords.iteritems():
        average_length = average_length + c.__len__() * freq[s]
    average_length = average_length / length
    for s, f in freq.iteritems():
        x = f / float(length)
        empirical_entropy = empirical_entropy + x * math.log(x, 2)
    print("Average code length: " + str(average_length))
    print("Empirical entropy: " + str(-empirical_entropy))
