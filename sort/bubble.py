#버블정렬 bubble sort
# O(n^2)
n = list(map(int, input().split()))

for i in range(n):
    for j in range(n - i  - 1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]

print(n)