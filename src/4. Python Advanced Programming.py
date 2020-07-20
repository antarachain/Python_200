#!/usr/bin/env python
# coding: utf-8

# In[44]:


f = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/stockcode.txt', 'r', encoding='CP949')
data = f.read()
print(data)
f.close()


# In[47]:


f = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/stockcode.txt', 'r', encoding='CP949')
line_num = 1
line = f.readline()
while line:
    print("%d %s" %(line_num, line), end='')
    line=f.readline()
    line_num += 1
f.close()


# In[49]:


f = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/stockcode.txt', 'r', encoding='CP949')
lines = f.readlines()
# print(lines)
for line_num, line in enumerate(lines):
    print('%d %s' %(line_num+1, line), end='')
f.close()


# In[53]:


text = input('파일에 저장할 내용을 입력하세요')
f = open('mydata.txt', 'w')
f.write(text)
f.close()


# In[55]:


count = 1
data = []
print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')
while True:
    text = input('[%d] 파일에 저장할 내용을 입력하세요:' %count)
    if text == '':
        break
    data.append(text+'\n')
    count += 1
    
f = open('mydata.txt','w')
f.writelines(data)
f.close()


# In[79]:


f = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/stockcode.txt', 'r')
h = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/stockcode_copy.txt', 'w')

data = f.read()
h.write(data)

f.close()
h.close()


# In[63]:


bufsize = 1024
f = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/img_sample.jpg', 'rb')
h = open('img_sample_copy.jpg', 'wb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)
    
f.close()
h.close()


# In[64]:


with open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/stockcode.txt', 'r')as f:
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1, line), end='')


# In[69]:


spos = 105
size = 500

f = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/stockcode.txt', 'r')
h = open('/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/stockcode_part.txt', 'w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close()
f.close()


# In[70]:


from os.path import getsize

file1 = '/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/5674-734/stockcode.txt'
file2 = '/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/img_sample_copy.jpg'
file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name: %s \t File Size: %d' %(file1, file_size1))
print('File Name: %s \t File Size: %d' %(file2, file_size2))


# In[74]:


from os import remove

target_file = '/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/stockcode_copy.txt'
k = input('[%s] 파일을 삭제하시겠습니까? (y/n)' %target_file)
if k == 'y':
    remove(target_file)
    print('[%s]를 삭제했습니다.' %target_file)


# In[80]:


from os import rename

target_file = '/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/stockcode_copy.txt'
newname = input('[%s]에 대한 새로운 파일이름을 입력하세요:' %target_file)
rename(target_file, newname)
print('[%s]->[%s]로 파일이름이 변경되었습니다.'%(target_file, newname))


# In[90]:


from os import rename

target_file = 'newname.txt'
newpath = input('[%s]를 이동할 디렉토리의 절대경로를 입력하세요:' %target_file)

if newpath[-1] == '/':
    newname = newpath + target_file
else:
    newname = newpath + '/' + target_file
    
try:
    rename(target_file, newname)
    print('[%s]->[%s]로 이동되었습니다.' %(target_file, newname))
except FileNotFoundError as e:
    print(e)


# In[1]:


import os, glob

folder = 'd:/devlab/py200'
file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files)
print(file_list)


# In[4]:


import os

pdir = os.getcwd(); print(pdir)
os.chdir('..'); print(os.getcwd())
os.chdir(pdir); print(os.getcwd())


# In[12]:


import os

newfolder = input("새로 생성할 디렉터리 이름을 입력하세요:")
try:
    os.mkdir(newfolder)
    print('[%s]디렉터리를 새로 생성했습니다.' %newfolder)
except Exception as e:
    print(e)


# In[8]:


import os

target_folder = 'new_folder'
k = input('[%s] 디렉터리를 삭제하겠습니까? (y/n)' %target_folder)

if k == 'y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제했습니다.' %target_folder)
    except Exception as e:
        print(e)


# In[13]:


import shutil
import os

target_folder =  '/Users/heoinhaeng/Desktop/coding/python/python_200/jupyter_notebook/new_folder'
print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.' %target_folder)
for file in os.listdir(target_folder):
    print(file)
k = input('[%s]를 삭제하시겠습니까? (y/n)' %target_folder)
if k == 'y':
    try:
        shutil.rmtree(target_folder)
        print('[%s]의 모든 하위 디렉터리와 파일들을 삭제했습니다.' %target_folder)
    except Exception as e:
        print(e)


# In[14]:


import os

from os.path import exists

dir_name = input('새로 생성할 디렉터리 이름을 입력하세요:')
if not exists(dir_name):
    os.mkdir(dir_name)
    print('[%s] 디렉터리를 생성했습니다.' %dir_name)
else:
    print('[%s]은(는) 이미 존재합니다.' %dir_name)


# In[15]:


import os
from os.path import exists, isdir, isfile

files = os.listdir()
for file in files:
    if isdir(file):
        print('DIR: %s' %file)
        
for file in files:
    if isfile(file):
        print('FILE: %s' %file)


# In[17]:


from time import localtime, strftime

logfile = 'test.log'
def writelog(logfile, log):
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'
    
    with open(logfile, 'a') as f:
        f.writelines(log)
        
writelog(logfile, '첫 번째 로깅 문장입니다.')


# In[28]:


from time import localtime

t = localtime()
start_day = '%d-01-01' %t.tm_year
elapsed_day = t.tm_yday

print('오늘은 [%s]이후 [%d]일째 되는 날입니다.' %(start_day, elapsed_day))


# In[29]:


from time import localtime

weekdays = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']

t = localtime()

today = '%d-%d-%d' %(t.tm_year, t.tm_mon, t.tm_mday)week = weekdays[t.tm_wday]

print('[%s]오늘은 [%s]입니다.' %(today, week))


# In[36]:


from datetime import datetime

start = datetime.now()
print('1에서 백만까지 더합니다.')
ret = 0
for i in range(1000001):
    ret += i
print('1에서 백만까지 더한 결과: %d' %ret)
end = datetime.now()
elapsed = end - start
print('총 계산 시간:', end='')
print(elapsed)
elapsed_ms = int(elapsed.total_seconds()*1000)
print('총 계산 시간:%dms' %elapsed_ms)


# In[40]:


num = input("아무 숫자를 입력하세요:")

if num.isdigit():
    num = num[::-1]
    ret = ''
    for i, c in enumerate(num):
        i += 1
        if i != len(num) and i%3 == 0:
            ret += (c + ',')
        else:
            ret += c
    ret = ret[::-1]
    print(ret)
else:
    print('입력한 내용[%s]: 숫자가 안비니다.' %num)


# In[42]:


text = input('문장을 입력하세요:')

ret = ''
for i in range(len(text)):
    if i != len(text)-1:
        ret += text[i+1]
    else:
        ret += text[0]

print(ret)


# In[43]:


url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=008&aid=0004442398&date=20200720&type=1&rankingSeq=5&rankingSectionId=101'

tmp = url.split('/')
domain = tmp[2]
print(domain)


# In[44]:


url = 'https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=008&aid=0004442398&date=20200720&type=1&rankingSeq=5&rankingSectionId=101'

tmp = url.split('/')
queries = tmp[1].split('&')
for query in queries:
    print(query)


# In[50]:


mystack = []

def putdata(data):
    global mystack
    mystack.append(data)
    
def popdata():
    global mystack
    if len(mystack) == 0;
        return None
    return mystack.pop()

putdata('데이터1')
putdata([3,4,5,6])
putdata(12345)

print('<스택상태>:', end='')
print(mystack)

ret = popdata()
while ret != None
    print('스택에서 데이터 추출', end='')
    print(ret)
    print('<스택상태>:', end='')
    print(mystack)
    ret = popdata()


# In[53]:


def getTextFreq(filename):
    with open(filename, 'r') as f:
        text = f.read()
        fa = {}
        for c in text:
            if c in fa:
                fa[c] += 1
            else:
                fa[c] = 1
    return fa

ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)
for c, freq in ret:
    if c == '\n':
        continue
    print('[%c]->[%d]회 나타남' %(c,freq))


# In[54]:


with open('mydata.txt', 'r') as f:
    data = f.read()
    tmp = data.split()
    print('단어수:[%d]' %len(tmp))


# In[58]:


def countWord(filename, word):
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower()
        pos = text.find(word)
        count = 0
        while pos != -1:
            count += 1
            pos = text.find(word, pos+1)
        return count
    
word = input('mydata.txt에서 개수를 구할 단어를 입력하세요:')
word = word.lower()
ret = countWord('mydata.txt', word)
print('[%s]의 개수: %d' %(word, ret))


# In[61]:


t1 = input('찾을 단어를 입력하세요:')
t2 = input('변경할 단어를 입력하세요:')

with open('mydata.txt', 'r') as f:
    with open('mydata2.txt', 'w') as h:
        text = f.read()
        text = text.replace(t1,t2)
        h.write(text)

print('[%s]를 [%s]로 변경하였습니다.' %(t1,t2))


# In[79]:


from urllib.request import urlopen

url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)


# In[80]:


from urllib.request import urlopen

url = 'https://www.python.org/'
with urlopen(url) as f:
    doc = f.read().decode()
    with open('pythonhome.html', 'w') as h:
        h.writelines(doc)


# In[86]:


from urllib.request import urlopen

imgurl = 'https://pds.joins.com/news/component/htmlphoto_mmdata/201702/21/7a7a6bf1-f27d-4799-adea-d609308820a6.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)


# In[87]:


from urllib.request import urlopen

BUFSIZE = 256*1024

fileurl = 'https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe'
filename = fileurl.split('/')[-1]
try:
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h:
            buf = f.read(BUFSIZE)
            while buf:
                h.write(buf)
                buf = f.read(BUFSIZE)
except Exception as e:
    print(e)


# In[89]:


filename = 'python-3.7.2.exe'
subsize = 1024*1024*3
suffix = 0

with open(filename, 'rb') as f:
    buf = f.read(subsize)
    while buf:
        subfilename = filename + '_' + str(suffix)
        with open(subfilename, 'wb') as h:
            h.write(buf)
            print('[%s]완료' %subfilename)
            
        buf = f.read(subsize)
        suffix += 1


# In[ ]:


# from zipfile import *

# def compressZip(zipname, filename):
#     print('[%s] -> [%s] 압축...' %(filename, zipname))
#     with ZipFile(zipname, 'w') as ziph:
#         ziph.write(filename)
        
#         print('압축이 끝났습니다.')
        
# filename = 'mydata.txt'
# zipzame = filename + '.zip'
# compressZip(zipname, filename)


# In[ ]:


# from zipfile import *
# import os

# def compressAll(zipname, folder):
#     print('[%s]->[%S]압축...' %(folder,zipname))
#     with ZipFile(zipname, 'w') as ziph:
#         for dirname, subdirs, files in os.walk(folder):
#             for file in files:
#                 ziph.write(os.path.join(dirname, file))
                
# folder = 'tmp'
# zipname = folder + '.zip'
# compressAll(zipname, folder)


# In[ ]:


# from zipfile import *

# def extractZip(zipname):
#     with ZipFile(zipname, 'r') as ziph:
#         ziph.extractall()
#         print('[%s]가 성공적으로 추출되었습니다.' %zipname)
        
# extractZip('file.zip')


# In[1]:


from random import shuffle
from time import sleep

gamenum = input('로또 게임 회수를 입력하세요:')

for i in range(int(gamenum)):
    balls = [x+1 for x in range(45)]
    ret = []
    for j in range(6):
        shuffle(balls)
        number = balls.pop()
        ret.append(number)
    ret.sort()
    print('로또번호[%d]:' %(i+1), end='')
    print(ret)
    sleep(1)


# In[7]:


from random import shuffle

male = ['슈퍼맨','심봉사','로미오','이몽룡','마루치']
female = ['원더우먼','뺑덕','줄리엣','성춘향','아라치']
shuffle(male)
shuffle(female)
couples = zip(male, female)

for i, couple in enumerate(couples):
    print('커플%d: [%s]-[%s]' %(i+1, couple[0],couple[1]))


# In[ ]:




