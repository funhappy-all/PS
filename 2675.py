N = int(input())

Tword =[]
Rword = []
for i in range(N):
    A, S = input().split()
    A = int(A)
    list_S = list(S)
    Word = []
    for j in range(len(list_S)):
        for k in range(A):
            Word.append(list_S[j])
    Tword.append([])
    Tword[i] += Word

for l in range(N):
    Rword.append([])
    Rword[l] = ''.join(Tword[l])
    print(Rword[l])