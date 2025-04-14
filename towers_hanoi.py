def move(n, source, target, auxiliary):
    # n - скільки дисків потрібно перемістити
    # source - звідки
    # target - куди
    #auxiliary - проміжний
    
    if n == 1:
        # якщо всього один диск - просто переміщаємо
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Перемістити диск {disk} з {source} на {target}")
        print("Проміжний стан:", towers)
    else:
        # крок 1: перемістити n-1 диск на auxiliary
        move(n-1, source, auxiliary, target)
        # крок 2: перемістити найнижчий диск на target
        move(1, source, target, auxiliary)
        # крок 3: перемістити n-1 диск з auxiliary на target
        move(n-1, auxiliary, target, source)

n = 5
towers = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

print("Початковий стан:", towers)
move(n, 'A', 'C', 'B')
print("Кінцевий стан:", towers)