vhod=input('vnesi zvok:  ')
stevec=0
for i in vhod:
    if i.lower()=='a' or i.lower()=='e' or i.lower()=='i'or i.lower()=='o' or i.lower()=='u':
        stevec+=1

print(stevec)

