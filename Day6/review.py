t = int(input())
for i in range(t):
    s = str(input())
    n1 = ""
    n2 = ""
    for j in range(0,len(s)):
        if j % 2 == 0:
            n1+= s[j]
        if j % 2 != 0:
            n2+= s[j]
    print(n1,n2)
