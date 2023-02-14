def answer():
    data = open('question.txt','r', encoding='UTF-8')  # открываем файл с вопросом
    que = data.readline()[11:len(data.readline())-1:] # записываем вопрос
    data.close() #закрываем файл
    
    file = open('answer.txt', 'r', encoding='UTF-8') # открываем файл с ответами
    for line in file:
        ans = set(line.split())  # множество со словами в строке
        if que in ans:           # ищем строку с ключевым словом и выводим его, если нашли то заканчиваем цикл
            print(line, end='')
            break

answer()

