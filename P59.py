import itertools

cipher = open('p059_cipher.txt', 'r')
encrypted = cipher.readlines()[0]
cipher.close()
encrypted = encrypted.rstrip('\n')
encrypted = encrypted.split(',')

for i in range(len(encrypted)):
    encrypted[i] = int(encrypted[i])

possibleKeys = itertools.permutations(range(97, 123), 3)
end = False
correctKey = (0,0,0)
decrypted = ""

while (not end):
    try:
        key = possibleKeys.next()
        plainText = ""
        for i in range(len(encrypted)):
            plainText += chr(encrypted[i] ^ key[i % 3])
        if (all(x in plainText for x in ["and ", "the "])):
            correctKey = key
            decrypted = plainText
    except StopIteration:
        end = True

res = 0
for c in decrypted:
    res += ord(c)
