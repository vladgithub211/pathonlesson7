n = int(input("Введите число=")) 
i=0
while n>0:
    n//=10   #n=n//10
    i+=1
print(f"Цифор в числе ----> {i}")

