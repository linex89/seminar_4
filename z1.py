# 25. Напишите программу, которая принимает на вход строку, и выводит кол-во повторов каждого из символов 1 раз.
s = list(input("введите строку "))
result = []
d = dict()
for i in s:
    count = 0
    if i in result:
        for j in result:
            if j == i:
                count += 1
        result.append(i)
        result.append(count)
    else:
        result.append(i)
        
print(result)