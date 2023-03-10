#!/usr/bin/env python
# coding: utf-8

# # Часть 1. Основы

# 001. Предложите пользователю ввести его имя 
# и выведите приветственное сообщение.
# Hello [имя]. 

# In[1]:


name = input('Введите имя: ')
print('Hello, ', name)


# 002. Предложите пользователю ввести его имя и фамилию, после чего выведите приветственное сообщение.
# Hello [имя] [фамилия].

# In[2]:


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
print('Hello, ', name, surname)


# 3. Напишите код, который выводит вопрос: «What do you call a bear with no teeth?», 
# а в следующей строке выводит ответ: «A gummy bear!» Попробуйте обойтись 
# одной строкой кода.

# In[5]:


print('What do you call a bear with no teeth?\nA gummy bear!')


# 4.Предложите пользователю ввести два числа. 
# Сложите эти числа и выведите результат в виде
# The total is [результат].

# In[10]:


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
print('The total is: ', num_1 + num_2)


# 5. Предложите пользователю ввести три числа. 
# Сложите первые два числа, затем умножьте сумму на третье число. 
# Выведите результат в виде
# The answer is [результат].

# In[12]:


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))
print('The total is: ', (num_1 + num_2) * num_3)


# 6. Cпросите, сколько кусков пиццы было у пользователя и сколько 
# кусков он съел. 
# Вычислите, сколько кусков пиццы у него осталось, и выведите результат в форме, 
# удобной для пользователя.

# In[15]:


slice_of_pizza_1 = int(input('Сколько кусков пиццы было: ')) 
slice_of_pizza_2 = int(input('Сколько кусков пиццы ты скушал: ')) 
print('Значит у тебя осталось: ', slice_of_pizza_1 - slice_of_pizza_2, 'Куска(ов)')


# 7. Предложите пользователю ввести его имя и возраст.
# 
# Увеличьте возраст на 1 и выведите сообщение:
# [имя] next birthday you will be [новый возраст].

# In[18]:


name = input('Введите имя: ')
age = int(input('Введите возраст: '))
print(name,',', 'next birthday you will be', age + 1)


# 8.Предложите пользователю ввести общую сумму счета, а затем запросите общее 
# количество участников обеда. 
# 
# Разделите сумму счета на количество участников 
# и выведите сумму, которую должен заплатить каждый участник.

# In[20]:


bill = int(input('Введите сумму счета: '))
persons = int(input('Введите количество участников: '))
print('Каждый должен внести: ', round(bill/persons, 2))


# 9. Напишите программу, которая предлагает ввести промежуток времени в днях, 
# а потом выводит количество часов, минут и секунд в этом промежутке

# In[22]:


days = int(input('Введите количество дней: '))
print('Hours:', days*24, 'Minutes:', days*24*60,'Seconds:', days*24*60*60)


# 10. В одном килограмме 2,204 фунта. 
# 
# Предложите пользователю ввести вес в килограммах и переведите его в фунты.

# In[25]:


kilo = int(input('Введите количество килограмм: '))
print('Pounds:', round(kilo*2.204,2))


# 11.  Предложите пользователю ввести число больше 100, а затем число меньше 10. 
# Сообщите, сколько раз меньшее число помещается в большем, в удобном формате.

# In[28]:


num_1 = int(input('Введите число больше 100: '))
num_2 = int(input('Введите число меньше 10: '))
print('Меньшее умещается в большем:', round(num_1/num_2, 0), 'раз(а)')


# # Конструкция if, Операторы сравнения, логические операторы

# 12.Предложите пользователю 
# ввести два числа. 
# 
# Если первое число больше второго, сначала выведите второе число, 
# а потом первое. 
# 
# В противном случае выведите сначала первое число, а потом второе

# In[29]:


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
if num_1 > num_2:
    print(num_2)
    print(num_1)
else:
    print(num_1)
    print(num_2)


# 13. Предложите пользователю ввести число, меньшее 20. 
# Если введенное число больше или равно 20, выведите сообщение «Too high»; 
# в противном случае выведите сообщение «Thank you».

# In[31]:


num = int(input('Введите первое число меньше 20: '))
if num >= 20:
    print('Too high')
else:
    print('Thank you')


# 14. Предложите пользователю ввести число от 10 до 20 (включительно). Если будет введено 
# число из этого диапазона, выведите сообщение «Thank you»; 
# в противном случае выведите сообщение «Incorrect answer»

# In[34]:


num = int(input('Введите число в интервале от 10 до 20 включительно: '))
if 10 <= num <= 20:
    print('Thank you')
else:
    print('Incorrect answer')


# 15. Предложите пользователю ввести любимый цвет. Если он введет «red», «RED» 
# или «Red», выведите сообщение «I like red too». В противном случае выведите сообщение «I don’t like [colour], I prefer red»

# In[38]:


colour = input('Write your favorite colour:')
if colour in ('Red', 'RED', 'red'):
    print('I like red too')
else:
    print("I don't like", colour)


# 16. Спросите пользователя, идет ли дождь. Преобразуйте его ответ к нижнему регистру. Если пользователь ответит «yes», спросите, ветрено ли на улице. Если пользователь ответит «yes» и на второй вопрос, выведите сообщение «It is too windy 
# for an umbrella»; в противном случае выведите сообщение «Take an umbrella». 
# Если же пользователь не дал положительного ответа на первый вопрос, выведите сообщение «Enjoy your day»

# In[42]:


answer_1 = input('Is it rain today?').lower()
if answer_1 == 'yes':
    answer_2 = input('Is it windy today?').lower()
    if answer_2 == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')


# 17.Предложите пользователю 
# ввести его возраст. Если 
# введенное значение равно 
# 18 и более, выведите сообщение «You can vote»; если 
# 17 — сообщение «You can 
# learn to drive»; если 16 — 
# сообщение «You can buy a 
# lottery ticket». Если значение 
# меньше 16, выведите сообщение «You can go Trickor-Treating»

# In[45]:


age = int(input('Your age: '))
if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trickor-Treating')


# 18. Предложите пользователю ввести число. Если оно меньше 10, выведите сообщение «Too low»; если число лежит в диапазоне от 10 
# до 20 — сообщение «Correct». В остальных случаях выведите сообщение «Too high».

# In[47]:


num = int(input('Введите число: '))
if num < 10:
    print('Low')
elif 10 <= num <= 20:
    print('Correct')
else:
    print('Too high')


# 19. Предложите пользователю ввести значение 1, 2 или 3. Если введено значение 1, выведите сообщение «Thank you»; если 2 — сообщение «Well done»; если 3 — сообщение «Correct». Если введено 
# любое другое значение, выведите сообщение «Error message»

# In[51]:


num = int(input("Enter 1, 2 or 3: "))
if num == 1:
 print("Thank you")
elif num == 2:
 print("Well done")
elif num == 3:
 print("Correct")
else:
 print("Error message")


# # Строки.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




