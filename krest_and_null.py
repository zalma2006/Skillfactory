##
def choise():
    print(f'Добрый день, это игра крестики нолики выберите режим игры')
    list_choise = ["Введите 1 чтобы начать играть:", "Введите 2 чтобы выйти из программы:"]
    print(f'{list_choise[0]: >40}')
    print(f'{list_choise[1]: >40}')
    return int(input())


def show(area):
    print(f'  | 0 | 1 | 2 |')
    print('-' * 15)
    for x, y in enumerate(area):
        row = f'{x} | {" | ".join(y)} |'
        print(row)
        print('-' * 15)


def ask(area):
    while True:
        cord = input('Ваш ход:').split()
        if len(cord) != 2:
            print('Вы ввели не верные координаты!')
            continue

        x, y = cord

        if not x.isdigit() or not y.isdigit():
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if x not in range(3) or y not in range(3):
            print('Координаты вне диапазона')
            continue
        if area[x][y] != ' ':
            print('Клетка занята')
            continue

        return x, y


def write(x, y, num, area):
    if num % 2 != 0:
        area[x][y] = 'X'
    else:
        area[x][y] = '0'


def check_win(area):
    win_list = [
        ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for cord in win_list:
        a = cord[0]
        b = cord[1]
        c = cord[2]
        if area[a[0]][a[1]] == area[b[0]][b[1]] == area[c[0]][c[1]] != ' ':
            return True
    return False


def game():
    chois = choise()
    while True:
        if chois == 1:
            win = ['Крестик', 'Нолик']
            area = [[' '] * 3 for i in range(3)]
            num = 0
            print('Приступим!')
            while chois == 1:
                show(area=area)
                num += 1
                if num % 2 != 0:
                    print('Ходит Крестик')
                else:
                    print('Ходит Нолик')
                x, y = ask(area=area)
                write(x=x, y=y, num=num, area=area)
                if check_win(area=area) == True:
                    show(area=area)
                    print(f'Выйграл {win[0] if num % 2 == 1 else win[1]}')
                    break
                if num == 9:
                    print('Ничья!')
                    show(area=area)
                    break
        elif chois == 2:
            print('До скорых встреч!')
            break
        else:
            continue
        second = input('Введите y чтобы сыграть ещё разок')
        if second.lower() == 'y':
            continue
        else:
            break



game()

##


##
