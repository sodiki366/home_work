from random import choice

student  = input('Представтесь,пожалуйста:')
try:
    level = int(input('Выберите уровень сложности 1-3:'))
except:
    level = 1
    print('Установлен первый уровень сложности')
if level < 1 or level >5:
    level =1
    print('Установлен первый уровень сложности')
print(f'Хорошо,{student},Тебе задачка!')
#Минимальное и максимальное число диапазона случайных чисел
min = 10 ** (level - 1)
max = 10 ** level - 1
points = 0
for i in range(5):
    #Первое слагаемое
    a = randint(min,max)
    #Второе слагаемое
    b = randint(min,max)
    print(f'{student},сколько будет {a} + {b}?', end='')
    correct_answer = a + b
    student_answer = input()
    if student_answer == str(correct_answer):
        points += 1
        print(f'Правильно!')
    else:
        print(f'Не правильно.Правильный ответ{correct_answer}')
if points == 5:
    print(f'Ах,ну какой умница,{student}.Это пять!')
elif points == 4:
    print(f'Молодец,{student},но можно лучше.Четыре.')
elif points == 3:
    print(f'Так себе,{student}.Садись, три.')
else:
    print(f'Два,{student},можешь садиться!')

