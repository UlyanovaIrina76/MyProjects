import numpy as np


def game_core_v3(number):
    '''Сначала устанавливаем random число, 
       а потом ищем его путем дробления ряда чисел от 1 до 100 на половины.
       Функция принимает загаданное число и возвращает число попыток'''
    
    count = 0   # количество попыток
    min_value = 0   # нижняя граница чисел - 1
    max_value = 101 # верняя граница чисел + 1
        predict = np.random.randint(1,101) # random число
    
    while number != predict:
        count += 1
        predict = (min_value + max_value)//2 # среднее между верхней и нижней границей
        if number > predict: 
            min_value = predict # если задуманное число > среднего устанавливаем новую нижнюю границу 
        elif number < predict: 
            max_value = predict # если задуманное число < среднего устанавливаем новую верхнюю границу 
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# запускаем
score_game(game_core_v3)