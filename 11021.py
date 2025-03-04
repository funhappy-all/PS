ca = []
T = int(input())
for i in range(0,T):
    a, b = map(int, input().split())
    ca.append(a+b)

for j in range(0,T):
    print("Case #" + str(j+1) + ": " +str(ca[j]))