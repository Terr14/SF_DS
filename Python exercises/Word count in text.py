# Попробуйте посчитать частоту каждого символа в следующем тексте:

# Как и в примере №4, предварительно очистите текст от символов переноса строки и 
# пробелов, приведите текст к нижнему регистру.

# В результате работы вашей программы у вас должен получиться словарь, 
# ключами которого являются символы, а значениями — их частота 
# (количество повторений в тексте).


text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""

text = text.lower()
text = text.replace('.', ' ')
text = text.replace(',', ' ' )
text = text.replace(';', ' ' )
text = text.replace('\n', ' ' )
print(text)
word_list = text.split(' ')
print(word_list)
count_dict = {}
for word in word_list:
    if word not in count_dict:
        count_dict[word] = 1
    else:
        count_dict[word] += 1
print(count_dict)
