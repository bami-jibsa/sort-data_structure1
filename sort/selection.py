#선택정렬 selection sort
#O(n^2)
n = list(map(int, input().split()))
for i in range(len(n)):
        a = i
        for j in range(i+1, len(n)):
                if n[a] > n[j]:
                        idx = j
        n[idx], n[i] = n[i], n[idx]