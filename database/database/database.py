from __future__ import print_function
import io  
import pandas as pd
i=0
b = 'C:/Users/user/Desktop/практика/RW.txt'
#d = 'C:/Users/user/Desktop/практика/new.txt'
print ('Введите данные:')
word = input()
print ('\n')
with io.open(b, encoding='utf-8') as file:
 for line in file:       
   nextline = next(file)
   nextli = next(file)
   if word in line:
     res = line + nextline +nextli
     print(res)
  
    # columns=['ID       ','ID_VK    ','Number    ','Mail               ',' Password     ']
    # print (columns)
    # print (res.strip().split(","))





#
#data = pd.read_csv(d, names=columns,sep=',',dtype=str) 
#print (data)    
#i=0
#b = 'C:/Users/user/Desktop/практика/database.txt'




        