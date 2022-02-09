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
    #predict_number = 1
    predict_number = np.random.randint(n_min, n_max)
    
    while True: # Выбирам число из середины диапазона, пока не угадаем
        
        count += 1
        n_mid = round((n_min+n_max) / 2)
        
        if n_mid == predict_number:
            return count
            
        else: 
            if n_mid > predict_number:
                n_max = n_mid
            
            elif n_mid < predict_number:
                n_min = n_mid

            if n_max - n_min == 1: # Если дошли до n_min=1 и n_min=2
                
                if n_max == predict_number:
                    count += 1
                    return count
                                    
                if n_min == predict_number:
                    count += 1
                    return count
    
       

def score_game(random_predict_v3) -> int:
    """За какое количсетво попыток в среднем за n подходов угадывает алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    n = 1000 # Количество повторений

    for number in range(n):
        count_ls.append(random_predict_v3())

    score = int(np.mean(count_ls))
    max_score = max(count_ls)
    print(f"Алгоритм угадывает число в среднем за: {score} попыток.\
        Количество повторений: {n}.\
        Максимальное количество попыток: {max_score}")
    return score

score_game(random_predict_v3)