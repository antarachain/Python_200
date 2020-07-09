#!/usr/bin/env python
# coding: utf-8

# In[94]:


int_data = 10
bin_data = 0b10
oct_data = 0o10
hex_data = 0x10
long_data = 1234567890123456789


# In[95]:


print(int_data)
print(bin_data)
print(oct_data)
print(hex_data)
print(long_data)


# In[96]:


f1 = 1.0
f2 = 3.14
f3 = 1.56e3
f4 = -0.7e-4


# In[97]:


print(f1)
print(f2)
print(f3)
print(f4)


# In[98]:


c1 = 1+7j
print(c1.real); print(c1.imag)
c2 = complex(2,3)
print(c2)


# In[99]:


a = 1
b = 2
ret = a+b
print('a와 b를 더한 값은', end='')
print(ret, end='')
print("입니다.")


# In[100]:


a = 2
b = 4
ret1 = a+b
ret2 = a-b
ret3 = a*b
ret4 = a/b
ret5 = a**b
ret6 = a+a*b/a
ret7 = (a+b)*(a-b)
ret8 = a*b**a                  # 거듭제곱은 사칙 연산보다 연산 순위가 더 우선합니다.


# In[101]:


print(ret1)
print(ret2)
print(ret3)
print(ret4)
print(ret5)
print(ret6)
print(ret7)
print(ret8)


# In[102]:


a = 0
a += 1
print(a)
a -= 5
print(a)
a *= 2
print(a)
a /= 4
print(a)


# In[103]:


a = True                   # True == 1
b = False                 # False == 0
print(a == 1)           # True가 출력됨
print(b != 0)           # False가 출력됨


# In[104]:


x = 1; y =2
str1 = 'abc';str2='python'
print(x==y)
print(x != y)
print(str1 == str2)
print(str2 == 'python')
print(str1 < str2)                        # 문자열의 크기 비교는 사전 순서로 비교한다.


# In[105]:


bool1 = True; bool2 = False; bool3 = True; bool4 = False
print(bool1 and bool2)
print(bool1 and bool3)
print(bool2 or bool3)
print(bool2 or bool4)
print(not bool1)
print(not bool2)


# In[106]:


strdata = 'abcde'                             # 문자열은 시퀀스 자료형임
listdata = [1,[2,3],'안녕']            # 리스트는 시퀀스 자료형임
tupledata = (100, 200, 300)      # 튜플은 시퀀스 자료형임


# In[107]:


strdata = 'Time is money!!'
listdata = [1,2,[1,2,3]]
print(strdata[5])
print(strdata[-2])
print(listdata[0])
print(listdata[-1])
print(listdata[2][-1])


# In[108]:


strdata = 'Time is money!!'
print(strdata[1:5])
print(strdata[:7])
print(strdata[:9])
print(strdata[:-3])
print(strdata[-3:])
print(strdata[:])
print(strdata[::2])


# In[109]:


strdata1 = 'I love'; strdata2='Python'; strdata3 = 'you'
listdata1 = [1,2,3]; listdata2 = [4,5,6]
print(strdata1 + strdata2)
print(strdata1 + strdata3)
print(listdata1 + listdata2)


# In[110]:


artist = 'BTS!'
fan = 'ARMY'
dispdata = fan + '들이 외칩니다.'+artist*3
print(dispdata)


# In[111]:


strdata1 = 'I love python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ['a','b','c', strdata1, strdata2]
print(len(strdata1))
print(len(strdata2))
print(len(listdata))
print(len(listdata[3]))


# In[112]:


listdata = [1,2,3,4]
ret1 = 5 in listdata           # False
ret2 = 4 in listdata           # True
print(ret1);print(ret2)
strdata = 'abcde'
ret3 = 'c' in strdata
ret4 = 'l' in strdata
print(ret3); print(ret4)


# In[113]:


strdata1 = '나는 파이썬 프로그래머다'
strdata2 = 'You are a programmer'
strdata3 = """I love
    python. too!
"""
strdata4 = "My son's name is John"
strdata5 = '문자열 "abc"의 길이는 3입니다.'


# In[118]:


txt1 = '자바'; txt2='파이썬'
num1 = 5; num2 = 10
print('나는 %s보다 %s에 더 익숙합니다.'%(txt1, txt2))
print('%s은 %s보다 %d배 더 쉽습니다.'%(txt2, txt1, num2))
print('%d + %d = %d' %(num1, num2, num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다.'%num1)


# In[121]:


from time import sleep
for i in range(100):
    msg = '\r진행률 %d%%'%(i+1)
    print(''*len(msg), end='')
    print(msg, end="")
    sleep(0.1)


# In[ ]:




