area = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ]
print(area)

def coordinates(area):
    print(f'Добрый день, это игра крестики нолики выберите режим работы:')
    list_choise = ["Введите 1 чтобы начать играть:", "Введите 2 чтобы выйти из программы:"]
    print(f'{list_choise[0]: 10}')
    print(f'{list_choise[1]: 10}')
    choise = input()
    return choise
coordinates(area=area)

# x = tuple(str(input('Введите координаты через запятую')).split(','))
# print(area, x)