import math
gc22,l23=map(int,input().split())
hp25=[]
tk12=list(map(int,input().split()))
for j in range(0,l23):
    rm12,mr32=map(int,input().split())
    hp25.append([rm12,mr32])
for j in hp25:
    y23=j[0]-1
    z24=j[1]-1
    print(math.gcd(tk12[y23],tk12[z24]))
