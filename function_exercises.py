#!/usr/bin/env python
# coding: utf-8

# In[182]:


# first we create a function is_two
def is_two(m):  
# we condition that if m=2 then
    if (m==2): 
#  the result will equal to True
        result= True
#  else if that m equal string 2
    elif (m=="2"):
#  the result will equal to True
        result=True
# we then exclude any other answers using else
    else:
# which the result should equal false
        result=False
# we then return the result
    return result


# In[183]:


# then verify that the code do what we meant it to do
is_two(6)


# In[184]:


is_two("2")


# In[185]:


is_two('ap')


# In[14]:


# define the function 
def is_vowel(m):
# identify the variable equal to vowel
    if m in list('AEIOUaeiou'):
# indicate the result should be True
        result=True
# condition that doesn't met
    else:
# the result will return false
        result=False
# indicate the return of result
    return result


# In[15]:


is_vowel('m')


# In[16]:


is_vowel('a')


# In[23]:


# define the function
def is_consonant(m):
# define the variable
    if m in list('AEIOUaeiou') or m.isdigit():
# identify that if the variable equal to vowel, the result will return false
        result=False
# set the else condition that if it is not vowel
    else:
# the result is true
        result=True
# return the result
    return result


# In[24]:


is_consonant('m')


# In[27]:


is_consonant('a')


# In[29]:


# the question asked to accept a string,when the string starts with consonant, capitalize the first word
def word(m):
#     for any character in the word
    for char in str(m):
#         if it starts iwth AEIOUaeiou, It will return a wanring and return the input
        if char in "AEIOUaeiou":
#         result equal a warning
            result=print("Your first letter starts with vowel, please try again with first letter with consonant")
#     result equal the input
            result=m
#     if condition not match as above 
        else:
#         result will return capitalize first word
            result=m.capitalize()
#     return the result
        return result


# In[31]:


word('word')


# In[108]:


word("an")


# In[126]:


# create a function to define the calculate_tip
def calculate_tip(tip,total):
#     create condition that if tip amount is greater than 1 or less than 0
    if tip<0 or tip>1:
#         the result will print out a message
        result=print('please enter a tip percentage number between 0-1')
#    if the above condition is not met
    else:
#       the result will return tip times total
        result=tip*total
#     return the result 
    return result


# In[127]:


calculate_tip(0.23,24.5)


# In[128]:


calculate_tip(1.23,24.5)


# In[135]:


# create a function that can apply the discount
def apply_discount(discount,total):
#    create a condition about the discount percentage
    if discount<0 or discount>1:
#         the result will print out a message
        result=print('please enter a discount percentage number between 0-1')
#    if the above condition is not met
    else:
#         the result should return total minus discounted price
        result=total-discount*total
#     return discount price
    return result


# In[137]:


apply_discount(.10,23)


# In[138]:


apply_discount(1.10,23)


# In[141]:


# create a function to define handle_commas
def handle_commas(m):
#     set condtion that any char in m
    for char in m:
#         that that char contains letter
        if char in"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefjhijklmnopqrstuvwxyz":
#         it will print a message
            mm=print('please input number')
#     else it will return the wanted result
        else:
#         using .replace to repalce "," with no result in order to remove ","
            mm=m.replace(",","")
#     return the result
    return mm


# In[142]:


handle_commas('21,')


# In[145]:


handle_commas("asa")


# In[146]:


handle_commas("12,121,832")


# In[194]:


# create a function to get a letter grade
def get_letter_grade(m):
#     set letter grade condition for A
    if m<=100 and m>=90:
#         if condition met, the result will print the message
        result=print('letter grade is A')
#     else it will run to second condition
    elif m<90 and m>=80:
#         if the second condition met, it will print the message
        result=print('letter grade is B')
#     if second is not met, it will run the third condition
    elif m<80 and m>=70:
#         if the third condition is met, print the message
        result=print('letter grade is C')
#     if the third condition is not met, try fourth condition
    elif m<70 and m>=60:
#         then print the fourth condition if it is met
        result=print('letter grade is D')
#     else it will return other message
    else:
#         set what other message
        result=print('You failed')
#     finanlly retunr the result
    return result


# In[195]:


get_letter_grade(90)


# In[196]:


get_letter_grade(80)


# In[197]:


get_letter_grade(0)


# In[35]:


# create a funciton that will remove vowel in a string
def remove_vowel(string):
    #     for any character in the string
    char = ('A''E''I''O''U''a''e''i''o''u')
#         if it starts iwth AEIOUaeiou, It will return a wanring and return the input
    for x in string:
        if x in char:
            newchar=string.replace(x,'')
    return newchar


# In[343]:


remove_vowel('July')


# In[36]:


remove_vowel('banana')


# In[41]:


import re
def normalize_name(m):
    m=re.sub(r"[^a-z0-9 ]","",m.lower())
    for mm in m:
        mm=m.replace(' ','_')
        return mm


# In[38]:


normalize_name('%Mdakl; jQwk am ')


# In[39]:


from itertools import accumulate


# In[47]:


def cumulative_sum(num):
    nn=[]
    return sum(num[:n] for n in num)


# In[48]:


cumulative_sum(1,2,3)


# In[ ]:





# In[ ]:




