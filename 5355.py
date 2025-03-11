C = int(input())
result = []
for i in range(0,C):
    data = input().split()
    N = float(data[0])

    for j in data[1:]:
        if j == "@":
            N = N * 3
        elif j == "%":
            N = N + 5
        elif j == "#":
            N = N - 7
    result.append(N)
for k in range(C):
    print(f"{result[k]:.2f}")