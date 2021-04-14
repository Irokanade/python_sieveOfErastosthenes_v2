while 1:
    try:
        n = int(input("Enter a number: "))
        if n < 2:
            continue
        else:
            break
    except:
        continue


prime = [True for i in range(n+1)]
result = []
p = 2
for p in range(2, n+1):
    if (prime[p] == True):
        result.append(p)
        for i in range(p * p, n+1, p):
            prime[i] = False

print(result)