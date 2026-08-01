usi=input('vnesi prvo vrsto:   ')
čas=input('vnesi čas simulacije:   ')

usi=usi.split()
for i in range(len(usi)):
    usi[i]=int(usi[i])

for d in range(int(čas)):
    spremembe = []
    for i in range(len(usi)):
        spremembe.append(0)
    
    for i in range(len(usi)):
        if usi[i]>=1 and usi[i] <=3:
            spremembe[i]=spremembe[i]+1
    for i in range(len(usi)):
        if i==len(usi)-1:
            if usi[i]>=5:
                spremembe[i]-=(usi[i] + 1) // 2
                spremembe[0]+=((usi[i] + 1) // 2)-1
        else:
            if usi[i]>=5:
                spremembe[i]-=(usi[i] + 1) // 2
                spremembe[i+1]+=(usi[i] + 1) // 2
    
    for i in range(len(spremembe)):
        usi[i]+=spremembe[i]
izhod=''
for i in range(len(usi)):
    izhod=izhod+str(usi[i])
    if i==len(usi)-1:
        pass
    else:
        izhod=izhod+' '
print(izhod)