# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# n = 123

# n1 = n // 100
# n2 = (n % 100) // 10
# n3 = n % 10
# res = n1 + n2 + n3 
# print(res)



# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.

# n = 50

# s = n // 3
# print(n // 6, n // 3 * 2 , n // 6)



# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

# n = 385926

# n1 = str(n)
# n2 = int(n1[0])
# n3 = int(n1[1])
# n4 = int(n1[2])
# n5 = int(n1[3])
# n6 = int(n1[4])
# n7 = int(n1[5])

# sum1 = n2 + n3 + n4
# sum2 = n5 + n6 + n7
# if sum1 == sum2:
#     print('yes')
# else:
#     print('no')



# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# a = 3
# b = 2
# c = 1

# if c % a == 0 or c % b == 0:
#     print('yes')
# else: 
#     print('no')