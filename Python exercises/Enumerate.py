# Условие задачи. У нас есть список ежедневной динамики числа пользователей приложения.

# Если элемент списка положительный, то число новых пользователей больше числа ушедших пользователей (прирост).
# Если элемент списка отрицательный, то число ушедших пользователей больше числа новых (отток).
# user_dynamics = [-5, 2, 4, 8, 12, -7, 5]
# Мы бы хотели вывести этот список на экран поэлементно в виде {номер дня}: {динамика}. 
# Например, для первого дня вывод должен быть "Day 1: -5".

user_dynamics = [-5, 2, 4, 8, 12, -7, 5] #заданный список динамики пользователей
#создаём цикл по индексам и элементам списка 
for i, dynamic in enumerate(user_dynamics): # i — индекс текущего элемента, dynamic — текущее значение из списка
    print("Day {} : {}".format(i+1, dynamic))
