print("1+2+3+...+n")
n = int(input("Введите конечное значение:"))
s=0
i=1
while i<=n:
    s+=i
    i+=1
    print("SUM", s)
print("Конечная сумма ", s)
