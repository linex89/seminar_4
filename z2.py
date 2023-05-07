# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.
text = input('введите текст ')
result = set()
start_word = 0
for i in range(len(text)):
    if text[i] == " ":
        result.add(text[start_word : i])
        start_word = i + 1
    elif i == len(text) -1:
        result.add(text[start_word : i+1])
result.discard(" ")
print(len(result))
        


