s = "Hello World111"
# print(s)
# wordlist = s.split()
# print(wordlist)

# print(len(wordlist[-1]))

l = len(s) - 1
print(l)

while l > 0:
    s1 = ''
    s1 = s1 + s[l]
    l -= 1

print(s1)