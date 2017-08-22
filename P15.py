currentLine = [1]*20
for l in range(20):
    currentLine[0] += 1
    for i in range(1,20):
        currentLine[i] = currentLine[i-1] + currentLine[i]

print currentLine[19]
        
