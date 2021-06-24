f = 'C:/Users/user/Desktop/практика/out_rw.txt'
b ='C:/Users/user/Desktop/практика/ysech.txt'
N=1000
with open(f) as data:
   c = open(b, 'w')
   for i in range(N):
        line = next(data).strip()
        print(line)
        c.write(line + '\n')

  for line in f:
     l = next(data).strip()      
      
      print(line)
f.close
print("end")

