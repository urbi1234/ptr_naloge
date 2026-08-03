n, m = input().split()
n = int(n)
m = int(m)

jezero = []

for i in range(n):
    jezero.append(input())

zgoraj = n
spodaj = 0
levo = m
desno = 0

for i in range(n):
    for j in range(m):
        if jezero[i][j] == "#":

            if i < zgoraj:
                zgoraj = i

            if i > spodaj:
                spodaj = i

            if j < levo:
                levo = j

            if j > desno:
                desno = j

visina = spodaj - zgoraj + 1
sirina = desno - levo + 1

obseg = 2 * visina + 2 * sirina

print(obseg)