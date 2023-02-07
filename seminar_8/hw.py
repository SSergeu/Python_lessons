def zad1():
    #В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
    #Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
    import random

    row = random.randint(4,8) # пусть будет от 4 до 7 групп

    student_scores = [None] * row  # список студентов
    average = [] # список средних арифм.

    for index in range(len(student_scores)):
        student_scores[index] = [random.randint(2,5) for _ in range(random.randint(20,30))] # случ. числа (оценки) от 2 до 5 
                                                                                    # в список из случ.числа (кол-ва студентов) от 20 до 30
    
    for i in range(len(student_scores)):                              # заполнение списка средним баллами групп
        N = sum(student_scores[i])/len(student_scores[i])
        N = round(N,2)                                                # округление ср. балла
        average.append(N)                                               

    for i in range(len(student_scores)):                              # вывод групп и их среднего балла
        print(f'{i+1}) {student_scores[i]} средний балл группы: {average[i]}')

    max_number = max(average) # максимальный элемент в списке с ср. баллами 
    max_index = 0             # максимальный индекс

    for i in range(len(average)):
        if average[i]==max_number:
            max_index=i

    print(f'{max_index+1} группа с наилучшим средним баллом = {max_number}')


def zad2():
    # Дана квадратная матрица, заполненная случайными числами. 
    # Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
    import random

    size_matrix = 4  # размер матрицы (например 4 на 4)
    diagonal = 0 

    matrix = [None] * 4
    sum_line = []

    for index in range(len(matrix)):           # запонлянем массив (список из списков в питоне)
        matrix[index] = [random.randint(1,10) for _ in range(size_matrix)]

    for i in range(len(matrix)): # заполнение списка суммой строк в матрице и подсчет сумму глав. диагонали 
        sum_line.append(sum(matrix[i])) 
        diagonal += matrix[i][i]
    
    for i in range(len(matrix)): # вывод матрицы и суммы элементов в строке
        print(f'{i}){matrix[i]} = {sum_line[i]}')
 
    print(f'Сумма главной диагонали = {diagonal}')
    print('Следующие строки больше суммы главной диагонали: ')

    m = True
    for i in range(len(sum_line)): # сравнение сумм с главной диагональю и вывод тех, что больше 
        if sum_line[i] > diagonal:
            print(i, end=' ')
            m = False

    if m: # вывод текста в случае, если все строки 
        print('Таких строк нет')

def zad3():
    # В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
    # Каждому месяцу соответствует своя строка
    # Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца. Выведите их даты.
    import random

    array = [None] * 5 # кол-во месяцев 5
    mount = ['май','июнь','июль','август','сентябрь'] # список с месяцами для вывода

    for index in range(len(array)): # заполняем списки случайными числами от 12 до 25 (средняя температура за день) 
        if index == 1 or index==4:
            array[index] = [random.randint(12,25) for _ in range(30)] 
        else:
            array[index] = [random.randint(12,25) for _ in range(31)]
    
    sum_max=[] # список в котором 7 жарких дней
    sum_min = [] # список в котором 7 холодных дней
    data = [] # список с датой (индексом) начала горячих или холодных дней

    for i in range(len(array)): # заполнение всех списков
        smax = 0
        smin = 25*7
        im = 0
        imin = 0
        for j in range(len(array[i])-6):
            seven = 0
            for l in range(7):
                seven += array[i][j+l]
            if seven > smax:
                smax = seven
                im = j+1
            if seven < smin:
                smin = seven
                imin = j+1
        sum_max.append(smax)
        sum_min.append(smin) 
        data.append(im)   
        data.append(imin)

    for i in range(len(array)): # вывод всех списков
        print(f'{mount[i]}: {array[i]}')
        print(f'сумма t самых жарких дней = {sum_max[i]}, с {data[i]} по {data[i]+7}; сумма t самых холодных дней = {sum_min[i]}, с {data[i+1]} по {data[i+1]+7}')

zad3()
