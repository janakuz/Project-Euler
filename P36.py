def isPalindrome(s):
    for i in range(len(s)/2+1):
        if (s[i] != s[len(s)-i-1]):
            return False
    return True


res = 0
for i in range(1000000):
    if (isPalindrome(str(i)) and isPalindrome(bin(i)[2:])):
        res += i
