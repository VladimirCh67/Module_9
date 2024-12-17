first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

f_res = []
for x in zip(first, second):
    f_res.append(x)

first_result = (abs(len(f_res[i][0]) - len(f_res[i][1]))
                for i in range(len(f_res)) if len(f_res[i][0]) != len(f_res[i][1]))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# print(list(zip(first, second)))
# print(f_res)
print(list(first_result))
print(list(second_result))
