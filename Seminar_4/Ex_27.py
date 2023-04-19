# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
#             подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится
#             в этом тексте.
#       Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells
#       sea shells on the sea shore I'm sure that the shells are sea shore shells
#      Output: 13

input_text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she " \
             "sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
words_list = []
word = ''
for i in range(len(input_text)):
    if input_text[i].isalpha() or input_text[i] == "'":
        word += input_text[i]
    else:
        words_list.append(word.upper())
        word = ''

unique_word_counter = len(set(words_list))
print(unique_word_counter)
print(set(words_list))

# Второй вариант
print(len(set(input_text.upper().split())))
