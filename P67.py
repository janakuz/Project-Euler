f = open('p067_triangle.txt', 'r')
pyramid = f.readlines()
f.close()
pyramid = [row.split(' ') for row in pyramid]
for row in range(len(pyramid)):
    pyramid[row] = [int(i) for i in pyramid[row]]

def maxPath(pyramid):
    for i in range(len(pyramid)-1, 0, -1):
        for j in range(1, len(pyramid[i])):
            pyramid[i-1][j-1] += max(pyramid[i][j-1], pyramid[i][j])
    return pyramid[0][0]
