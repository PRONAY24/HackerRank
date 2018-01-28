n = int(input())
li = []
num = 0
k = 1
i = 0
j = 1
y = input()
li.append(y)
while True:
    if j == n:
        i += 1
        j = i+1
    if k < n:
        z = input()
        li.append(z)
        k += 1
    if i==n-1:
        break
    x = str(li[i]+li[j])
    #print(x)
    j += 1
    if '0' in x:
        if '1' in x:
            if '2' in x:
                if '9' in x:
                    if '3' in x:
                        if '4' in x:
                            if '5' in x:
                                if '6' in x:
                                    if '7' in x:
                                        if '8' in x:
                                            num += 1
                                            #print('yes')
print(num)
