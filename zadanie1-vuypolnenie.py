print("Модуль 1 часть 1")

print("№1")
value = float
value = ((7 * 5) / 8 + 5) / (3 ** 5)
print(value)
print("-----------------------------")

print("№2")
b = 109
v = int(input("Введите скорость байка"))
t = int(input("Введите время поездки"))
print((v * t) % b)
print("-----------------------------")

print("№3")
ch1 = float(input())
ch2 = float(input())
max1 = (ch1 > ch2) * ch1 + (ch2 >= ch1) * ch2
print(max1)
print("-----------------------------")

print("Модуль 1 часть 2")

print("№1")
a = int(input('1 число: '))
b = int(input('2 число: '))
c = int(input('3 число: '))
if a == b == c:
	print(3)
elif a == b or b == c or a == c:
	print(2)
else:
	print(0)
print("-----------------------------")

print("№2")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
	print("YES")
else:
	print("NO")
print("-----------------------------")

print("№3")
password = False
password = str
while password != True:
	password = input("Введите пароль из 8 любых букв: ")
	lenia = len(password)
	if lenia >= len("aaaaaaaa"):
		print("пароль успешно создан")
		password = True
	else:
		print("ошибка, попробуйте снова! ")
print("-----------------------------")
