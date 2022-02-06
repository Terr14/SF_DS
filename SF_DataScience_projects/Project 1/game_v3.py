
import numpy as np

def random_predict_v3(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    n_min = 1
    n_max = 101
    count = 0
    number = np.random.randint(n_min, n_max)        
    while True: # Выбирам число из середины диапазона, пока не угадаем
        count += 1
        n_mid = round((n_min+n_max)/2) 
        if n_mid > number:
            n_max = n_mid
        
        elif n_mid < number:
            n_min = n_mid

        else:
            return count
       

def score_game(random_predict_v3) -> int:
    """За какое количсетво попыток в среднем за n подходов угадывает алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    n = 100 # Количество повторений

    for number in range(n):
        count_ls.append(random_predict_v3())

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за: {score} попыток.\
        Количество повторений: {n}")
    return score

score_game(random_predict_v3)