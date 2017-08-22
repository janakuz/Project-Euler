f = open('P18.txt', 'r')
pyramid = f.readlines()
f.close()
pyramid = [row.split(' ') for row in pyramid]
for row in range(len(pyramid)):
    pyramid[row] = [int(i) for i in pyramid[row]]

def maxPath(pyramid):
    if (len(pyramid) == 1):
        return pyramid[0][0]
    
    leftPyramid = [1]*(len(pyramid)-1)
    rightPyramid = [1]*(len(pyramid)-1)
    
    for i in range(1, len(pyramid)):
        leftPyramid[i-1] = pyramid[i][:i]
        rightPyramid[i-1] = pyramid[i][1:]
    
    leftMax = maxPath(leftPyramid)
    rightMax = maxPath(rightPyramid)
    return pyramid[0][0] + max(leftMax, rightMax)
        
