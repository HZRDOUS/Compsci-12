path = 0
a = 0
lst = []

n = int(input("Enter your number here:"))

#for n in range(1, 30):
while n != 1:
    a = n
    if n % 2 == 1:
        n = n * 3 + 1
    else:
        n = n / 2

    lst.append(n)
    path += 1

print(path)
print(max(lst))