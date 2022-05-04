import random #для генеарции кто ходит первым - крестик или нолик
#создаем игровое поле,3 списка по 3 элемента, храним состояния тут, "внутренняя память"
playField = [[" "] * 3 for i in range(3)]
#визиалузируем игровую сетку
def grid():
    print(" | 0 | 1 | 2 | ")
    print('---------------')
    print (f'0| {playField[0][0]} | {playField[0][1]} | {playField[0][2]} |')
    print('---------------')
    print (f'1| {playField[1][0]} | {playField[1][1]} | {playField[1][2]} |')
    print('---------------')
    print (f'2| {playField[2][0]} | {playField[2][1]} | {playField[2][2]} |')
    print('---------------')
#прописываем логику запроса позиции от игрока. И проверяем доступность позиции хода
def turn():
    while True:
        try:
            x, y = map(int, input('Твой ход: ').split())
            if 0>x or x>2 or 0>y or y>2:
                print("Вне диапазона, попробуй еще")
                continue
            if playField[x][y] != " ":
                print("Клетка занята")
                continue
            return x, y
            break
        except ValueError: #обрабатываем отличные от int ошибки
            print('ты чо,дурак? Введи корректное значение координаты!')
            x, y = map(int, input('Твой ход: ').split())
            if 0>x or x>2 or 0>y or y>2:
                print("Вне диапазона, попробуй еще")
                continue
            if playField[x][y] != " ":
                print("Клетка занята")
                continue
            return x, y
#основной цикл программы
counter = 1 #нумерация хода для человека,не для программиста
state = random.randint(1,10) #генерируем кто ходит
print('Тебе не повезло сыграть в наискучнейшее задание.')
print('Оно хоть и дает много на подумать, но выполнять его банально неинтересно.')
while True:
    print(f'Ход {counter}')
    counter +=1
    grid()
    if state%2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')
    state += 1
    x, y = turn()
    if counter%2 == 1:
        playField[x][y] = 'x'
    else:
        playField[x][y] = '0'
    #на текущем ходу првоерка на выигрышные условия для х. Возможно запись можно  разбить на много строк меньшей длины,но забыл как
    if playField[0][0] == playField[0][1] == playField[0][2] == 'x' or playField[1][0] == playField[1][1] == playField[1][2] == 'x' or playField[2][0] == playField[2][1] == playField[2][2] =='x' or playField[0][0] == playField[1][0] == playField[2][0]=='x' or playField[0][1] == playField[1][1] == playField[2][1]=='x' or playField[0][2] == playField[1][2] == playField[2][2] == 'x' or playField[0][0] == playField[1][1] == playField[2][2] =='x' or playField[2][0] == playField[1][1] == playField[0][2]=='x':
        print( f'Победа крестика на {counter} ходу!')
        break
    #на текущем ходу првоерка на выигрышные условия для 0. Возможно запись можно  разбить на много строк меньшей длины,но забыл как
    if playField[0][0] == playField[0][1] == playField[0][2] == '0' or playField[1][0] == playField[1][1] == playField[1][2] == '0' or playField[2][0] == playField[2][1] == playField[2][2] =='0' or playField[0][0] == playField[1][0] == playField[2][0]=='0' or playField[0][1] == playField[1][1] == playField[2][1]=='0' or playField[0][2] == playField[1][2] == playField[2][2] == '0' or playField[0][0] == playField[1][1] == playField[2][2] =='0' or playField[2][0] == playField[1][1] == playField[0][2]=='0':
        print(f'Победа нолика на {counter} ходу!')
        break
    if counter == 10:
        print('Ничья')
        break

