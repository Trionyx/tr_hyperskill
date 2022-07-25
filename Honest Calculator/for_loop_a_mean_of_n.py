n = int(input())
a = []
for _ in range(n):
    x = int(input())
    a.append(x)
c = a.count()
print((sum(a))/c)
