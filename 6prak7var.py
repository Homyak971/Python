# Задание 1
import random
data = []
for _ in range(10):
    data.append(random.randint(0, 100))
print("Входные данные:", data)
summ = 0
prois = 1
for i in data[1:10:2]:
    summ += i
for i in data[0:10:2]:
    prois *= i    
print("Сумма:", summ)
print("Произведение:", prois)

# Задание 2
import random
data = []
for _ in range(10):
    data.append(random.randint(0, 100))
min = max = 0
for i in range(10):
    if data[min] > data[i]:
        min = i
    if data[max] < data[i]:
        max = i
print("Входные данные:\t\t", data)
data[min], data[max] = data[max], data[min]
print("После перестановки:\t", data)
