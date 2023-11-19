import random
#latihan buat presen
Xr = random.random()
epsilon = 0.001
max_iter = 200

for i in range(1, max_iter + 1):
    Xrplus1 = (14 - Xr**2) / 5
    e = abs(Xrplus1 - Xr)
    if e < epsilon:
        print(f'Konvergensi tercapai: gx = {Xrplus1:.6f} setelah {i} iterasi')
        break
    Xr = Xrplus1
else:
    print(f'Konvergensi tidak tercapai setelah {max_iter} iterasi')
