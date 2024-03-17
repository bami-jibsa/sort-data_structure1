#삽입정렬 insert sort
#O(n^2)
n = list(map(int, input().split()))
for i in range(1, len(n)):
    for j in range(i, 0, -1):
        if n[j-1] > n[j]:
            n[j-1], n[j] = n[j], n[j-1]    
            print(n)        

print(n)