import pika
import numpy as np
from sklearn.datasets import load_diabetes
# Загружаем датасет о диабете
X, y = load_diabetes(return_X_y=True)
# Формируем случайный индекс строки
random_row = np.random.randint(0, X.shape[0]-1)