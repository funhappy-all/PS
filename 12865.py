# W, V를 이차원 배열로 입력받고, 길이만큼 반복, 

N = int(input("\n")) #number of object
K = int(input("\n")) #
wv = []
C = []

#물건 무게(W), 가치(V) 배열로 입력받기
for i in range(0,N):
    w, v = map(int, input("").split())
    wv.append([w,v])

# 탐색 과정
n_wv = len(wv) 

for j in range(0,n_wv):
    