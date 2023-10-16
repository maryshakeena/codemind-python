
W, X, Y, Z = map(int, input().split())
possible = False
for i in range(2):
    for j in range(2):
        for k in range(2):
            if i * X + j * Y + k * Z == W:
                possible = True
                break
if possible:
    print("YES")
else:
    print("NO")
