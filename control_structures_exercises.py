#!/usr/bin/env python
# coding: utf-8

# In[9]:


# when today is Monday
week = False
if week:
    print('it is Monday')
else:
    print ('it is not Monday')


# In[10]:


#  when today is weekday
weekday=True
if weekday:
    print('it is weekday')
else:
    print('it is not weekday')


# In[1]:


#  create a variable that calculate the total and when working hour greater than 40 the extra hours equal to 1.5 times hourly rate
hour_worked=41
hourly_rate=30
total = hour_worked*hourly_rate
if hour_worked>40:
    total =(hour_worked-40)*(hourly_rate*1.5)+(40*hourly_rate)
print(total)


# In[2]:


# create a while loop when i =5 and i+1 while i is less and equal to 15
i = 5
while i <= 15:
    print(i)
    i += 1


# In[3]:


# create a while loop that will count by 2s
i=0
while i <=100:
    print(i)
    print('------')
    i += 2


# In[8]:


# alter loop to count backwards by 5s from 100 to -10
i=100
while i >= -10:
    print(i)
    print('------')
    i -= 5


# In[16]:


# alter loop to start with 2 and display the number square on each line while the number is less than 1,000000
i=2
while i <=1000000:
    print(i)
    print('------')
    i **= 2


# In[17]:


# alter loop to count backwards by 5s from 100 to 5
i=100
while i >= 5:
    print(i)
    print('------')
    i -= 5


# In[36]:


# creating a float/int for output to times from 1-10
n=float(input())
for i in range(1,11):
    print(n,'x',i,'=',i*n)


# In[35]:


# creating for loop with prescribed answer
for i in range(1,10):
    for k in range (1,i+1):
        print(i,end="")
    print()


# In[114]:


# Creating a for loop to skip ipput odd number
n=int(input("Number to skip is: ")) 
number=n
for n in range(1,50):
    if n%2!=0 and n!=number:
        print("Here is an odd number: ",n)
    if number==n:
        print('Yikes!Skipping number: ',n)
        continue
        break


# In[209]:


n=int(input("your input: "))
for number in range(n+1):
    print(number)
if n ==str():
    print("Please enter valid number")


# n=int(input("your input: "))
# for number in range(n+1):
#     print(reversed(number))

# In[131]:


n=int(input("your input: "))
for number in reversed(range(n)):
    n1=number+1
    print(n1)


# In[132]:


#  write a program counting from 1-100
for n in range (1,101):
    print(n)


# In[140]:


number=int(input("Your input Number"))
if number %3==0:
    print('Fizz')
else:
    print(number)


# In[143]:


number=int(input("Your input Number"))
if number %5==0:
    print('Buzz')
else:
    print(number)


# In[145]:


number=int(input("Your input Number"))
if number %5==0 and number %3==0:
    print('FizzBuzz')
else:
    print(number)


# In[231]:


from tabulate import tabulate
n=int(input('What number would you like to go up to? '))
print('Here is your table!')
while True:
    table=[['number','square','cubed'],[n,n**2,n**3]]
    print(tabulate(table))
    n=int(input('enter number to continue, otherwise type"00" to stop'))
    if n == 00:
        print('Okay,bye!')
        break


# In[235]:


n=float(input('Please enter your grade: '))
while True:
    if n>100:
        print ('Please enter number between 1-100')
    if n<=100 and n>=88:
        print("Your letter grade is A")
    if n<88 and n>=80:
        print("Your letter grade is B")
    if n<80 and n>=67:
        print("Your letter grade is C")
    if n<67 and n>=60:
        print("Your letter grade is D")
    if n<60 and n>=0:
        print("Your letter grade is F")
    n=int(input('enter number to continue, otherwise type"00" to stop'))
    if n == 00:
        print('Okay, Bye!')
        break


# In[314]:


book=dict({'title':'1984', 'author':'George Orwell','genre':"Dystopian Fiction"})
print(book)


# In[316]:


book=[{'title':'1984', 'author':'George Orwell','genre':"Dystopian Fiction"}]
b=input('Please enter the book genres: ')        
while True:
    if b=='Dystopian Fiction':
        print(f"{book['title']} is your book")
    b=input('Please enter the book genres: ')


# In[ ]:




