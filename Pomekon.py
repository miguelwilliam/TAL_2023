N = int(input())
pomekons = []
for i in range(N):
    pomekon = input()
    if pomekon not in pomekons:
        pomekons.append(pomekon)

print(f'Falta(m) {151-len(pomekons)} pomekon(s).')