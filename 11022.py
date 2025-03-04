al = []
bl = []
ca = []
T = int(input())
for i in range(0,T):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)
    ca.append(a+b)

for j in range(0,T):
    print("Case #" + str(j+1) + ": " +str(al[j])+ " + "+str(bl[j])+" = "+str(ca[j]))