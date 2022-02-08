a = "aaaaabbbccddd"
li = list(a)

d = {}

for c in li:
    #print(c)
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
print(d["b"])
