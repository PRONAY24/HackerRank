def f(k,a,b):
    s = 0
    #so = 0
    i=1
    while a <= b:
        s += i
        i *= k
        s= s%(10**9 +7)
        i+=1
        #print("s= ",s)
        if i>a:
            #so = so+s
            #print("so=",so)
            i = 1
            a += 1
    return s%(10**9 + 7)
size = int(input())
for i in range(size):
    k,a,b = input().split()
    k,a,b = int(k),int(a),int(b)
    print(f(k,a,b))
