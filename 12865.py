#Dynamic programing을 활용.

N, K = map(int, input().split())
item = []
kg=[]
for i in range(0,N):
    W, V = map(int, input().split())
    item.append([W,V])

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = item[i-1]
    for weight in range(K+1):
        if w>weight:
            dp[i][weight] = dp[i-1][weight]
        else:
            dp[i][weight] = max(dp[i-1][weight], dp[i-1][weight - w]+v)

print(dp[N][K])