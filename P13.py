f = open('P13.txt', 'r')
summands = f.readlines()
f.close()
summands = [long(i) for i in summands]
largeSum = sum(summands)
print str(largeSum)[:10]
