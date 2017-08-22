import functools
import locale

import locale
locale.setlocale(locale.LC_ALL, 'english') # vary depending on your lang/locale
assert sorted((u'Ab', u'ad', u'aa'), cmp=locale.strcoll) == [u'aa', u'Ab', u'ad']

f = open('p022_names.txt', 'r')
names = f.read()
f.close()
names = names.split(',')
names = [oldName.replace('"', "") for oldName in names]
names = sorted(names, key=functools.cmp_to_key(locale.strcoll))

letterValues = {}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1, 27):
    letterValues.update({alphabet[i-1]:i})

sumNames = 0
for i in range(len(names)):
    sumName = 0
    for j in range(len(names[i])):
        sumName += letterValues[names[i][j]]
    sumNames += sumName*(i+1)
