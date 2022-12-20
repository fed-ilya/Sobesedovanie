f = open('1942.txt.TXT')
s = f.readline()
chisla = ['1','2','3','4','5','6','7','8','9','0']
mas_s_imenami = ['Мистер A','Мистер B','Мистер C','Мистер D','Мистер F']
mas_name = ['A','B','C','D','F']
mas_del = ['S','D','R','C']
uchastniki = [0] * 5 #Для решения 1 номера(Кто сколько раз был замечен за непотребными занятиями)
nabludenia = [] * 5  #0- Мистер A, 1- Мистер B, 2- Мистер C, 3- Мистер D, 4- Мистер F
chastota_nar = [0] * 5

for i in range(5): #Каждому человеку приписываем массив из его занятий(Создаем двумерный массив)
    nabludenia.append ([0] * 4) #0- Sex, 2- Drugs, 3- Rock-N-Roll, 4- Cigarettes

i = 0

while i != len(s)-7:
    k = 2
    chislo = ''
    uchastniki[mas_name.index(s[i])] += 1
    if s[i+1] == "D":
        chastota_nar[mas_name.index(s[i])] += 1
    while (s[i+k] in chisla):
        chislo += s[i+k]
        k += 1
    nabludenia[mas_name.index(s[i])][mas_del.index(s[i+1])] += int(chislo)
    i += k
    
print("Наблюдения-", nabludenia)
print("Сколько каждый участник группы был замечен-", uchastniki)

maxk = 0
name = ''
for i in range(5):
    if uchastniki[i] > maxk:
        maxk = uchastniki[i]
        name = mas_s_imenami[i]
print("1 задание: ", name)

maxrock = 0
minrock = 10000000
for i in range(5):
    if maxrock < nabludenia[i][2]:
        maxrock = nabludenia[i][2]
    if minrock > nabludenia[i][2]:
        minrock = nabludenia[i][2]
delta = maxrock - minrock
print("2 задание:", delta)

maxnar = 0
name_nar = ''
for i in range(5):
    if chastota_nar[i] > maxnar:
        maxnar = chastota_nar[i]
        name_nar = mas_s_imenami[i]
print("3 задание: ", name_nar,",", nabludenia[mas_s_imenami.index(name_nar)][2], "граммов", nabludenia[mas_s_imenami.index(name_nar)][2] // maxnar, "-средняя доза")