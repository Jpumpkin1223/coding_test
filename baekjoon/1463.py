n = int(input())
min_list = [0] * (10**6 + 1)

for i in range(2, n + 1):
    min_list[i] = min_list[i - 1] + 1
    if i % 2 == 0:
        min_list[i] = min(min_list[i], min_list[i // 2] + 1)
    if i % 3 == 0:
        min_list[i] = min(min_list[i], min_list[i // 3] + 1)

print(min_list[n])
