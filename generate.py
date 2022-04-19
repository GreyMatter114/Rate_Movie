import sys,random,pickle
def display(n,l):
    f=open("Store.txt",'w',encoding='utf-8')
    for i in range(0,n):
        for j in l:
          if(j=="Overall"):
            o=input("Enter Overall")
            f.write(f'Overall:{o}\n')
            continue
          x=round(random.randint(1,5))
          print(f'{j}:{x}\n')
          f.write(f'{j}:{x}\n')
    f.close()
def Convert(tup):
    di=dict()
    for a,b in tup:
        di.setdefault(a, []).append(b)
    return di
l=["Script","Technique","VFX","Direction","Acting","Overall"]
n=int(input("Enter no of movies"))
display(n,l)
file = open("Store.txt", "r")
file_lines = file.readlines()
file.close()
required = [tuple(map(str, i.split(':'))) for i in file_lines]
di=Convert(required)
for i in (l):
    for j in range(n):
        di[i][j]=int(di[i][j][0])
