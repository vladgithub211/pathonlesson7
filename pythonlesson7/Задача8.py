while True:             # бесконечный цикл
    k = int(input("Введите k (не более 15): "))
    if k<=15: break      # выход из цикла
# вычисление факториала
p = 1          # начальное знач. произвед.
i = 1          # начальное знач. множителя
while True:    # начало цикла
    p = p*i    # добавить к произведению
    i = i+1    # следующее знач. множителя
    if i>k: break      # конец цикла при i>k
print("Факториал числа равен", p)
