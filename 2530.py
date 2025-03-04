A, B, C = map(int, input().split())
D = int(input())

A1 = D//3600
B1 = (D%3600)//60
C1 = ((D%3600)%60)

A2 = A+A1
B2 = B+B1
C2 = C+C1

if C2>=60:
    C2  = C2-60
    B2+=1
if B2>=60:
    B2 = B2-60
    A2+=1
while A2>=24:
    A2 = A2-24

print(A2, B2, C2)