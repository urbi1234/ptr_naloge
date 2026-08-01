#1. naloga Milina Ura --- Urban Skuk

vhod=input('Vpisi stevilo ali niz:   ')
vhod=vhod.split()
izhod=''
for i in range(len(vhod)):
    try:
        vhod[i]=int(vhod[i])
    except ValueError:
        print('Vpisani znaki niso stevila')
        quit()

for i in vhod:
    if i%2==0:
        izhod=izhod+'Tik'
    else:
        izhod=izhod+'Tak'
        
print(izhod)