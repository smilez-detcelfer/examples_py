# debug:
Shift + F9
F8 - 1 шаг
F9 - скачок до метки

a = 10  # int
b = 5.3 # float
s = 'string 123' # str
s = input() # ввод строки

# деление на цело: '//'
# остаток от деления: '%'
float_var = 3.14
int(float_var) # округление числа до нижней границы (3)
str(float_var) # '3.14'
bool(float_var) # False, если '' или 0, в других случаях True
bool_var = 'a' in str_var # вернёт bool, вместо str_var может быль любой itterable объект

if bool:
    # code1
elif bool:
    # code2
else:
    # code in else
# код после ветвления

запуск из linux:
python script.py
или
chmod +x script.py
#! /path/to/python_bin в начале файла
./script.py # оболочка смотрит в шебанг с помощью какого бинарника запускать файл

itterable:
строка - неизменяемый itterable
str_var = 'abc'
str_var[1] = '2' #выдаст ошибку

str_var[0:3] # срез
str_var[3:] # до конца
str_var[0:4:2] # срез с шагом
str_var[-1::-1] # срез от последнего символа до первого (перевернутая строка)

#методы строк:
str_var.upper() / .lower()
str_var.split("split_symbol", 3) превращает строку в массив строк 2ой параметр указывает кол-во сплитов
", ".join(itterable) соединяет itterable в строку с разделителем ", "
str_var.find("lol") - вернёт индекс первого вхожедния подстроки в str_var
str_var.rfind(("l")) как find, но ищет справа на лево
str_var.index("lol") то же что find, но если нет совпадения - вернёт ошибку
str_var.rindex(("l")) как index, но ищет справа на лево
str_var.count() кол-во вхождений
str_var.strip() убирает спецсимволы и пробелы в начале и конце строки
str_var.replace("target", "new")

# сортировка по результату выполнения функции
def foo(element):
    return len(element)
s = sorted(list, key=foo, reverse=True) #reverse для переворачивания результата


# циклы

while i < 10:
    # code in cycle
        break # выбрасывает из цикла, else не отработает
else:
    # отработет если выйдет из while по условию i < 10

for i in str_var: # i принимает элемент в строке
for i in range(10): # i принимает число от 0 до 9
break # выход из цикла
continue # пропустить код внутри цикла до следующей иттерации

sp = ["smth", "bla", 123, "qq"] # список, изменяеммый itterable
sp.append("new_elem")
sp.pop(<element_index>)
sp = [i for i in range(100) if i % 2 == 0 ]
dic = {'key': 'huita', vasya: 'mudel'} # ключ - неизменяемый объект, значение - любой объект
dic.items() # делает список состоящих из кортежей (ключ, значение)
dic.keys # список ключей
dic.values() # список значений
dic.get("no_key") # вернёт None, если ключа нет |
dic.get("no_key", 'return this if no key')
for i in dic
    print(i, dic[i])
for k, v in dic.items(): # распаковка картежа
    print(k, v)

sp = {1, 'lol', True} # множество уникальных значений
set(sp) # привести к множеству

a | b # объединение множеств
a - b # вычитание множеств
a & b # входящие в оба множества
a ^ b # не входящие в оба множества
a.add(33) # добавит в множество
a.issubset({1,2,3,4}) # является ли подмножеством
a.issuperset({1,2,3})

file = open("filename", "r") # открыть на чтение
sp = []
for line in file:
    print(line,strip())
    sp.append(line.strip())

s = file.readlines() # возвращает список всех строк из файла (list)
#-------------------
file = open("filename", "w") # открыть на запись
file = open("filename", "w+") # открыть на добавление в конец файла

for i in range(10):
    file.write(sp[i]+"\n")

#-------------------
print(f'formated string! Put variable here {var}')
print('Formated string! String var here: %s, Number here: %d' % ("string", var))
print('ip is {ip}, port is {port}'.format(ip="192.168.1.1", port = 8080))
#-------------------
def function1(x, y):
    return(x - y)
#!!!При передаче переменной в виде аргумента функции,
# если переменная меняется внутри функции - она изменится снаружи:
sp = [1, 1, 2, 3, 5]
def change_list(list):
    list[0] = 100
change_list(sp)
#sp = [100, 1, 2, 3, 5]

def foo(arg1, arg2):
    return(result)
foo() - вызов функции
foo - ссылка на объект в памяти (объект)


#Именнованые параметры:
function1(y = b, x = a) # уже не важен порядок аргументов, т.к. они указаны явно
#Параметры п умолчанию:
def function1(x=0, y=0):
    return(x - y)
#Если параметр не указан - будет использован параметр по умолчанию
print(function1(y = 5))

#Произвольное количество параметров:
def foo(*args)
    return(sum(args))
sum_res = foo(1,2,3)
print(sum_res)

sp = ["masha", 123, "192.168.1.1"]
#s = "name:{} id:{} ip:{}".format(sp[0],sp[1],sp[2])
s = "name:{} id:{} ip:{}".format(*sp)
#в *sp передаются элементы списка по порядку

#Распаковка словаря в именнованные параметры:
def foo(x = 0, y = 0, z = 0):
    return(x*y*z)
d = {'x':1, 'y':2, 'z':3}
print(foo(**d)) # ключи словаря должны совпадать с названиями аргументов функции

#распаковка словаря в позиционные параметры функции:
def foo(x, y, z):
    return(x*y*z)
d = {'x':1, 'y':2, 'z':3}
print(foo(*d))
#Произвольное количество именованных параметров:
def foo(a = 0, b = 0, *args, **kwargs):
    print("parameters:")
    print("a=",a)
    print("b=", b)
    print(args)
    print(kwargs)
    print('z =', kwargs.get('z'))
    return(a * b)
foo(1,2,3,4,5,6, z = 12, y = 13)


#область видимости
с = 100
def foo(x):
    c = x + 1 # создается локальная переменная c, это не та же переменная что и глобальная
    return x - 1
#---------------
с = 100
def foo(x):
    global c # говорит, что дальше будет использована глобальная переменная с, объявленная ранее
    nonlocal  # используется для использования внутри внутренней функции указывая на переменную во внешней функции
    c = x + 1
    return x - 1

#Внутренняя функция может захватывать аргументы из внешней функции
def external(a):
    def internal(b):
        print(a+b)
#------------------
#lambda функции
list = ['Sasha', 'Lena', 'Gregor', 'Suliman']
def f(v):
    return len(v)
 f = lambda v: len(v) # функция в одну строку, одноразовая
list = sorted(list, key=lambda v: len(v))
#------------------
#MAP:
sp = ['1', '2', '3', '4', '5', '6', '7']
#превратим в список чисел без map:
for i in range(len(sp)):
    sp[i] = int(sp[i])+100
#превратим в список чисел с map:
sp = list(map(lambda item : int(item) + 100, sp))
# map нужно оборачивать в list или во что-либо ещё.
#------------------
#FILTER
sp = [1, 2, 3, 4, 5, 6]
res = filter(lambda x: x >= 4, sp)
print(list(filter))
#------------------
# сначала отфильтруем, потом отфильтрованные элементы умножим на 2
sp1 = [1, 2, 3, 4, 5, 6, 44, 22, 11, 48]
res1 = map(lambda x: x*2, filter(lambda y: y > 20, sp1))
print(list(res1))
#------------------
#ZIP
sp1 = [1, 2, 3, 4, 5]
sp2 = ['a','b','c','d']
z = zip(sp1, sp2)
list(z) #=> = [(1, 'a'),(2, 'b'),(3, 'c')]
#------------------
#reduce
sp1 = [1, 2, 3, 4, 5]
functools.reduce(lambda r, n: r + n, sp1)
# применяет функцию на соседние элементы в списке, записывает результат, применяет к следующему элементу
#------------------
#модули
if __name__ == '__main_':
    print('Програма запущена сама по себе')
else:
    print('этот модуль импортирован')

import module
module.smth
from module import smth
smth()
dir(module) # покаже список имен в модуле
dir() # в текущем модуле
#-------------------
#OS
# вывод stdout\stderr нельзя отловить в переменные
os.system("ls -la")

# принимает список из команды и ей аргументов
subprocess.call("ls")
subprocess.call("ls -la") #упадет с ошибкой
subprocess.call(["ls"],["-la"]) # отработает корректно
subprocess.call("ls -la", shell=True) # выполнится оболочкой

p = subprocess.run('dir', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(p.stdout.decode())
print(p.stderr.decode())

ipconfig_result = subprocess.check_output('ipconfig')
print(ipconfig_result.decode('windows-1252'))

p = subprocess.Popen(['ping', '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait() # ожидание завершения процесса
print(p.stdout.read().decode())

# ввести stdin и забрать stdout
p = subprocess.Popen(['python.exe', 'stdin_out.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
out, err = p.communicate(input=b"3\n5\n7\nexit") # вводятся байты
print(out.decode())
#-------------------

os.getcwd()
os.mkdir('./my_dir')

#-------------------
try:
    a = '123'
    b = a // 2
    print('should i print it?')
except Exception as e:
    print('exception here')
finally:
    print('finally')
print('program end')
#-------------------
#create class
class Person:
    name = ''
    age = None
p = Person

#set name value to instance
setattr(p, 'name', 'Vasya')
#or
p.name = 'Vasya'

#return name value of instance:
getattr(p, 'name')
#-------------------

