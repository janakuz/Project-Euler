grid = []
for i in range(2):
    newline = []
    for j in range(8):
        newline += [1]
    grid += [newline]
for i in range(2,201):
    newline = []
    newline += [1]
    for j in range(1,8):
        newline += [0]
    grid += [newline]


coins = [1,2,5,10,20,50,100,200]

for i in range(2,201):
    for ind in range(1,8):
        grid[i][ind] = grid[i][ind-1]
        grid[i][ind] += grid[i-coins[ind]][ind]
