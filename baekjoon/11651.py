n = int(input())
n_list = []
for _ in range(n):
    x, y = map(int, input().split())
    n_list.append((x, y))

n_list.sort(key=lambda x: (x[1], x[0]))

for i in n_list:
    print(*i)
