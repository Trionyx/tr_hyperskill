i = input()
t = []
p = ""
for char in i:
    if char.isupper():
        t.append("_")
        t.append(char.lower())
    else:
        t.append(char)
for char in t:
    p = p + char
print(p)
