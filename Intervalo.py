N = int(input())
dentro = 0
fora = 0
for i in range(N):
    num = int(input())
    if num <= 20 and num >= 10:
        dentro+=1
    else:
        fora+=1

print(dentro, 'in')
print(fora, 'out')