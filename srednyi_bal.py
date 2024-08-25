grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5,2],[4, 4, 3], [5, 5, 5, 4, 5]]
#Расчет среднний бал для первого( нулевого) значения [5, 3, 3, 5, 4]
#print(type(grades))
a = grades[0] #Присваиваем переменной «а» значение оценок [5, 3, 3, 5, 4]
len_a = len(grades[0]) #Через команду “len” считаем количество оценок(символов)
sum_a = sum(a) #Через команду “sum” считаем общую сумму всех оценок
arithmetic_mean_a = sum_a / len_a #Данной переменной присваем значение средней арифметической оценке полученное по данной формуле
#print(arithmetic_mean_a)
#Расчет среднний бал для второго(первого) значения [2, 2, 2, 3] выполная тежи действия что и с первым( нулевым) значением
b = grades[1]
len_b = len(grades[1])
sum_b = sum(b)
arithmetic_mean_b = sum_b / len_b
#print(arithmetic_mean_b)
#Расчет среднний бал для третьего( второго) значения [4, 5, 5,2] выполная тежи действия что и с первым( нулевым) значением
c = grades[2]
len_c = len(grades[2])
sum_c = sum(c)
arithmetic_mean_c = sum_c / len_c
#print(arithmetic_mean_c)
#Расчет среднний бал для четвертого( третьего) значения [4, 4, 3] выполная тежи действия что и с первым( нулевым) значением
d = grades[3]
len_d = len(grades[3])
sum_d = sum(d)
arithmetic_mean_d = sum_d / len_d
#print(arithmetic_mean_d)
#Расчет среднний бал для пятого( четвертого) значения [5, 5, 5, 4, 5] выполная тежи действия что и с первым( нулевым) значением
e = grades[4]
len_e = len(grades[4])
sum_e = sum(e)
arithmetic_mean_e = sum_e / len_e
#print(arithmetic_mean_e)

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print(type(students)) т.к. множество не является упорядоченной последовательностью, нужно перевести в другой тип.
list_stedents = list(students) # множество переводим в тип списки 'list' для дальней реботы с ним.
#print(type(list_stedents))
#print(list_stedents)
#Сортируем по алфовиту
sorted_list_students = sorted(list_stedents)
#print(sorted_list_students)
# задаем переменную для каждого студента
aa = sorted_list_students[0]
bb = sorted_list_students[1]
cc = sorted_list_students[2]
dd = sorted_list_students[3]
ee = sorted_list_students[4]
# Создаем словарь по окончании всех расчетов и операций
dict_end = dict({aa: arithmetic_mean_a, bb: arithmetic_mean_b, cc: arithmetic_mean_c, dd: arithmetic_mean_d, ee: arithmetic_mean_e})
print(dict_end)