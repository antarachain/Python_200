#!/usr/bin/env python
# coding: utf-8

# In[35]:


print("안녕하세요")


# In[36]:


print("안녕하세요")
a = 1
b = 1
print(a+b)


# In[37]:


_myname = 'samsjang'
my_name = '홍길동'
MyName2 = "Hong gil-dong"
counter = 1
Counter = 2


# In[38]:


import keyword
keyword.kwlist


# In[39]:


number1 = 1
pi = 3.14
flag = True
char = 'x'
chars = 'I love Python'


# In[40]:


number = 1
number+2


# In[41]:


number = 'one'
number


# In[42]:


# 주석 처리 예시임
# 만든 날짜: 2016.5.30
a = 1
b = 5
print(a+b)


# In[43]:


"""
a=1
b=5
print(a+b)
"""
a = 2
b = 6
print(a+b)


# In[44]:


int_data = 1                                           # 정수 선언
float_data = 3.14                                # 실수 선언
complex_data = 1+5j                        # 복소수 선언
str_data1 = 'I love Python'              # 문자열 선언
str_data2 = "반갑습니다."                  # 문자열 선언
list_data = [1,2,3]                              # 리스트 선언
tuple_data = (1,2,3)                          # 튜플 선언 
dict_data = {0:'False', 1:'True'}   # 딕셔너리 선언


# In[45]:


a = 200
msg = "I love Python"
list_data = ['a','b','c']
dict_data = {'a':97, 'b':98}
print(a)
print(msg)
print(list_data)
print(list_data[0])
print(dict_data)
print(dict_data['a'])


# In[46]:


print('#', end="")
print('#')


# In[47]:


listdata = ['a','b','c']

if 'a' in listdata:
    print('a가 listdata에 있습니다.')
    print(listdata)
else:
    print('a가 listdata에 존재하지 않습니다.')


# In[48]:


if 'a' in listdata: print('a가 listdata에 있습니다.')


# In[49]:


x = 1
y = 2
if x>=y:
    print('x가 y보다 크거나 같습니다.')
else:
    print('x가 y보다 작습니다.')


# In[50]:


x = 1
y = 2

if x>y:
    print('x가 y보다 큽니다.')
elif x<y:
    print('x가 y보다 작습니다.')
else:
    print('x와 y가 같습니다.')


# In[51]:


scope = [1,2,3,4,5]
for x in scope:
    print(x)


# In[52]:


str = 'abcdef'

for c in str:
    print(c)


# In[53]:


list = [1,2,3,4,5]

for c in list:
    print(c)


# In[55]:


ascii_codes = {'a':97, 'b':98, 'c':99}

for c in ascii_codes:
    print(c)


# In[59]:


for c in range(10):
    print(c)


# In[60]:


scope = [1,2,3,4,5]

for x in scope:
    print(x)
    if x < 3:
        continue
    else:
        break


# In[61]:


scope = [1,2,3,4,5]

for x in scope:
    print(x)
    if x>=3:
        break


# In[65]:


scope = [1,2,3]

for x in scope:
    print(x)
#     break
else:
    print('Perfect')


# In[66]:


x = 0
while x < 10:
    x = x+1
    if x<3:
        continue
    print(x)
    if x > 7:
        break


# In[67]:


x = 1
total = 0
while 1:
    total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x=x+1


# In[70]:


val = None
condition = 1
if condition ==1:
    val = [1,2,3]
else:
    val = 'I love python'
val

