
N, K, X, Y = map(int, input().split())
cost1 = K * X + (N - K) * Y
cost2 = N * X
print(min(cost1, cost2))
