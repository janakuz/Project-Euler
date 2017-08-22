f = open('p042_words.txt', 'r')
words = f.readlines()
words = words[0].split(',')
words = [w.replace('"', '') for w in words]
f.close()


def isTriangle(n):
    i = 1
    while (n > 0):
        n -= i
        i += 1
    return n == 0

letterVals = {}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(alphabet)):
    letterVals[alphabet[i]] = i+1


triangleWords = 0
for word in words:
    wordVal = 0
    for letter in word:
        wordVal += letterVals[letter]
    if (isTriangle(wordVal)):
        triangleWords += 1


