#!/usr/bin/env python
# coding: utf-8

# In[164]:


k = input('이름을 입력하세요')
print('당신이 입력한 이름은 <'+k+'>입니다.')


# In[165]:


numdata = 57
strdata = '파이썬'
listdata = [1,2,3]
dictdata = {'a':1, 'b':2}

def func():
    print('안녕하세요.')
    
print(type(numdata))
print(type(strdata))
print(type(listdata))
print(type(dictdata))
print(type(func))


# In[166]:


a = 11113
b = 23
ret = a%b            # 나눗셈에서 나머지만 구하기(%)
print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.' %(a,b,ret))


# In[167]:


a = 11113
b = 23
ret1, ret2, = divmod(a,b)           # 몫과 나머지 구하기
print('<%d/ %d>는 몫이 <%d>, 나머지가 <%d>입니다.' %(a,b,ret1,ret2))


# In[168]:


h1 = hex(97)
h2 = hex(98)
ret1 = h1 + h2
print(ret1)
a = int(h1, 16)
b = int(h2, 16)
ret2 = a+b
print(hex(ret2))


# In[169]:


abs1 = abs(-3)
abs2 = abs(-5.72)
abs3 = abs(3+4j)
print(abs1)
print(abs2)
print(abs3)


# In[170]:


ret1 = round(1118)
ret2 = round(16.554)
ret3 = round(1118, -1)
ret4 = round(16.554, 2)
print(ret1)
print(ret2)
print(ret3)
print(ret4)


# In[171]:


idata1 = int(-5.4)
idata2 = int(1.78e1)
idata3 = int(171.56)
print(idata1)
print(idata2)
print(idata3)


# In[172]:


fdata = float(10)
print(fdata)


# In[173]:


def getPrime(x):
    if x%2 == 0:
        return
    
    for i in range(3, int(x/2), 2):
        if x%i == 0: 
            break
            
        else:
            return x
        
listdata = [117,119,1113,11113,11119]
ret = filter(getPrime, listdata)
print(list(ret))


# In[174]:


def getPrime(n):
    ret = [2]
    if n <= 2:
        return ret
    
    for i in range(3, n+1, 2):
        for k in range(3, int(i/2), 2):
            a = i%k
            if a == 0:
                break
            else:
                ret.append(i)
    
    return ret

ret = getPrime(10)
print(ret)


# In[175]:


listdata = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
maxval = max(listdata)
minval = min(listdata)
print(maxval)
print(minval)

txt = 'Alotofthingsoccureachday'
maxval = max(txt)
minval = min(txt)
print(maxval)
print(minval)

maxval = max(2+3, 2*3, 2**3, 3**2)
minval = min('abz','a12')
print(maxval)
print(minval)


# In[176]:


a = 107
b = a&0x0f
print(b)


# In[177]:


a = 107
b = (a>>4)&0x0f
print(b)


# In[21]:


txt1 = "A tale that was not right"
txt2 = '이 또한 지나가리라.'
print(txt1[5])
print(txt2[-2])


# In[22]:


txt1 = "A tale that was not right"
txt2 = '이 또한 지나가리라.'
print(txt1[3:7])
print(txt2[:6])
print(txt2[-4:])


# In[23]:


txt = 'python'
for i in range(len(txt)):
    print(txt[:i+1])


# In[24]:


txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2]
print(ret)


# In[25]:


ret = txt[1::2]
ret


# In[26]:


txt = 'abcdefghijk'
ret = txt[::-1]
print(ret)


# In[27]:


ret = txt[::-2]
print(ret)


# In[28]:


ret = txt[-2::-2]
print(ret)


# In[30]:


filename = input("저장할 파일이름을 입력하세요:")
filename = filename + '.jpg'
display_msg = '당신이 저장한 파일은 <'+filename+'> 입니다.'
print(display_msg)


# In[31]:


msg1= '여러분'
msg2 = '파이팅!'
display_msg = msg1+','+msg2*3+'~!'
print(display_msg)


# In[32]:


msg = input('임의의 문장을 입력하세요.')
if 'a' in msg:
    print('당신이 입력한 문장에는 a가 있습니다.')
else:
    print('당신이 입력한 문장에는 a가 없습니다.')


# In[33]:


msg = input('임의의 문장을 입력하세요:')
if 'is' in msg:
    print('당신이 입력한 문장에는 is가 있습니다.')
else:
    print('당신이 입력한 문장에는 is가 없습니다.')


# In[34]:


msg = input('임의의 문장을 입력하세요')
msglen = len(msg)
print('당신이 입력한 문장의 길이는 <%d>입니다.' %msglen)


# In[35]:


txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'
ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()
print(ret1)
print(ret2)
print(ret3)
print(ret4)


# In[36]:


txt1='010-1234-5678'
txt2='R2D2'
txt3='1212'
ret1=txt1.isdigit()
ret2=txt2.isdigit()
ret3=txt3.isdigit()
print(ret1)
print(ret2)
print(ret3)


# In[37]:


txt1='안녕하세요?'
txt2='1.TItle-제목을 넣으세요'
txt3='3피오R2D2'
ret1=txt1.isalnum()
ret2=txt2.isalnum()
ret3=txt3.isalnum()
print(ret1)
print(ret2)
print(ret3)


# In[38]:


txt = 'A lot of Things occur each day.'
ret1=txt.upper()
ret2=txt.lower()
print(ret1)
print(ret2)


# In[39]:


txt = '     양쪽에 공백이 있는 문자열입니다.     '
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()
print('<'+txt+'>')
print(txt)
print('<'+ret1+'>')
print(ret1)
print('<'+ret2+'>')
print(ret2)
print('<'+ret3+'>')
print(ret3)


# In[40]:


numstr = input('숫자를 입력하세요:')
try:
    num = int(numstr)
    print('당신이 입력한 숫자는 정수<%d>입니다.'%num)
except:
    try:
        num=float(numstr)
        print('당신이 입력한 숫자는 실수<%f>입니다.'%num)
    except:
        print("+++숫자를 입력하세요~ +++")


# In[41]:


num1 = 1234
num2 = 3.14

numstr1 = str(num1)
numstr2 = str(num2)
print('num1을 문자열로 변환한 값은 "%s"입니다.' %numstr1)
print('num2를 문자열로 변환한 값은 "%s"입니다.' %numstr2)


# In[42]:


txt = "A lot of things occur each day, every day."
word_count1 = txt.count('o')
word_count2 = txt.count('day')
word_count3 = txt.count(' ')
print(word_count1)
print(word_count2)
print(word_count3)


# In[43]:


txt = 'A lot of things occur each day, every day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day',30)
print(offset1)
print(offset2)
print(offset3)


# In[44]:


url = 'http://www.naver.com/news/today=20160831'
log='name:홍길동 age:17 sex:남자 nation:조선'

ret1 = url.split('/')
print(ret1)

ret2 = log.split()
for data in ret2:
    d1, d2 = data.split(':')
    print('%s -> %s' %(d1,d2))


# In[45]:


loglist = ['2016/08/26 10:12:11', '200', 'OK', '이 또한 지나가리라']
bond = ';'
log = bond.join(loglist)
print(log)


# In[46]:


txt = 'My password is 1234'
ret1 = txt.replace('1','0')
ret2 = txt.replace('1','python')
print(ret1)
print(ret2)

txt = '매일 많은 일들이 일어납니다.'
ret3 = txt.replace('매일','항상')
ret4 = ret3.replace('일','사건')
print(ret3)
print(ret4)


# In[47]:


u_txt = 'I love python'
b_txt = u_txt.encode()
print(u_txt)
print(b_txt)

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1)
print(ret2)


# In[48]:


b_txt = b'A lot of things occur each day.'
u_txt = b_txt.decode()
print(u_txt)


# In[81]:


strdata = input('정렬할 문자열을 입력하세요:')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True)
print(ret1)
print(ret2)
ret1 = "".join(sorted(ret1))
ret2 = "".join(ret2)


# In[69]:


range1 = range(10)
range2 = range(10, 20)
print(list(range1))
print(list(range2))


# In[71]:


ret = 0
for i in range(10):
    ret += (i+1)
print(ret)


# In[72]:


listdata = [1,2,'a','b','c',[4,5,6]]
val1 = listdata[1]
val2 = listdata[3]
val3 = listdata[5][1]
print(val1)
print(val2)
print(val3)


# In[74]:


solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성', '지구']
planet = '지구'
pos = solarsys.index(planet)
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
pos = solarsys.index(planet, 5)
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))


# In[75]:


solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
planet = '화성'
pos = solarsys.index(planet)
solarsys[pos] = 'Mars'
print(solarsys)


# In[83]:


solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
rock_planets = solarsys[1:4]
gas_planets = solarsys[4:]
print('태양계의 암석형 행성:', end=''); print(rock_planets)
print('태양계의 가스형 생성:', end=''); print(gas_planets)


# In[84]:


listdata = list(range(1,21))
evenlist = listdata[1::2]
print(evenlist)


# In[85]:


oddlist = listdata[0::2]
print(oddlist)


# In[86]:


listdata = list(range(5))
listdata.reverse()
print(listdata)


# In[87]:


listdata = list(range(5))
ret1 = reversed(listdata)
print('원본 리스트', end=''); print(listdata);
print('역순 리스트', end=''); print(list(ret1))

ret2 = listdata[::-1]
print('슬라이싱 이용', end='');print(ret2)


# In[91]:


listdata1 = ['a','b','c','d','e']
listdata2 = ['f','g','h','i','j']
listdata3 = listdata1+listdata2
listdata4 = listdata2+listdata1
print(listdata3)
print(listdata4)


# In[92]:


listdata = list(range(3))
ret = listdata*3
print(ret)


# In[94]:


listdata = []
for i in range(3):
    txt = input('리스트에 추가할 값을 입력하세요[%d/3]:' %(i+1))
    listdata.append(txt)
    print(listdata)


# In[99]:


solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
pos = solarsys.index('목성')
print(pos)
solarsys.insert(pos, '소행성')
print(solarsys)


# In[106]:


solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del solarsys[0]
print(solarsys)
del solarsys[-2]
print(solarsys)


# In[110]:


solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
solarsys.remove('태양')
print(solarsys)


# In[113]:


solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del solarsys[1:3]
print(solarsys)


# In[114]:


listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
listsize = len(listdata)
print(listsize)


# In[115]:


listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
c1 = listdata.count(2)
c2 = listdata.count(7)
print(c1)
print(c2)


# In[124]:


listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
del listdata
print(listdata)


# In[128]:


namelist = ['Mary','Sams','Aimy','Tom','Michale','Bob','Kelly']
namelist.sort()        # 알파벳순 정렬
namelist.sort(reverse=True) # 알파벳순 역순 정렬
print(namelist)


# In[129]:


namelist = ['Mary','Sams','Aimy','Tom','Michale','Bob','Kelly']
ret1 = sorted(namelist)
ret2 = sorted(namelist, reverse=True)
print(namelist)
print(ret1)
print(ret2)


# In[138]:


from random import shuffle

listdata = list(range(1,11))
for i in range(3):
    shuffle(listdata)
    print(listdata)


# In[143]:


solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
ret = list(enumerate(solarsys))
print(ret)

for i, body in enumerate(solarsys):
    print('태양계의 %d번째 천체: %s' %(i,body))


# In[144]:


listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
ret = sum(listdata)
print(ret)


# In[146]:


listdata1 = [0,1,2,3,4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
print(all(listdata1))
print(any(listdata1))
print(all(listdata2))
print(any(listdata2))
print(all(listdata3))
print(any(listdata3))


# In[149]:


solar1=['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
solar2 = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Nepture']
solardict = {}
for i, k in enumerate(solar1):
    val = solar2[i]
    solardict[k] = val
    
print(solardict)


# In[153]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
names['Aimy'] = 10000
print(names)


# In[154]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
del names['Sams']
print(names)


# In[155]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
names.clear()
print(names)


# In[202]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ks = names.keys()
print(ks)

for k in ks:
    print('Key : %s \t Value : %d' %(k, names[k]))


# In[183]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
vals = names.values()
print(vals)

vals_list = list(vals)
print(vals_list)
ret = sum(vals_list)
print('출생아 수 총계: %d' %ret)


# In[184]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
items = names.items()
print(items)

for item in items:
    print(item)


# In[205]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
k = input('이름을 입력하세요:')


if k in names:
    print('이름이 <%s>인 출생아 수는 <%d>명입니다.' %(k, names[k]))
else:
    print('자료에 <%s>인 이름이 존재하지 않습니다.' %k)


# In[18]:


names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ret1 = sorted(names)
print(ret1)

def f1(x):
    return x[0]

def f2(x):
    return x[1]
    
ret2 = sorted(names.items(), key=f1)
print(ret2)

ret3 = sorted(names.items(), key=f2)
print(ret3)

ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret4)


# In[21]:


ch = input('문자를 1개 입력하세요:')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('문자: %s \t코드값: %d[%s]'%(ch, chv, hex(chv)))


# In[25]:


val = input("문자 코드값을 입력하세요:")
val = int(val)
try:
    ch = chr(val)
    print('코드값: %d[%s], 문자:%s' %(val,hex(val), ch))
except ValueError:
    print('입력한<%d>에 대한 문자가 존재하지 않습니다!' %val)


# In[27]:


expr1 = '2+3'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('<%s>를 eval()로 실행한 결과:' %expr1, end=''); print(ret1)
print('<%s>를 eval()로 실행한 결과:' %expr2, end=''); print(ret2)


# In[31]:


add = lambda x,y: x+y
ret = add(1,3)
print(ret)

funcs = [lambda x: x+'.pptx', lambda x:x+'.docx']
ret1 = funcs[0]('intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ret3 = sorted(names.items(), key=lambda x:x[0])
print(ret3)


# In[32]:


f = lambda x: x*x
args = [1,2,3,4,5]
ret = map(f, args)
print(list(ret))


# In[34]:


f = lambda x,y: x*x+y
X = [1,2,3,4,5]
Y = [10,9,8,7,6]
ret = map(f,X,Y)
print(list(ret))


# In[ ]:




