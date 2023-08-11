# Write a python program create csv file student.csv(sid,sname,city,contact) using 10 records 
##(in which 5 records input directly and 5 records take input from user). write records into this file.

import csv
q=open('c:\\22bca221\\python\\student2.csv','w',newline='')
w=csv.writer(q)
head=['sid','sname','city','contact']
w.writerow(head)

#five records input directly.
rows=[[1,'om','surat',7835657845],[2,'sai','rajkot',94567456],[3,'radha','mumbai',7465645],[4,'ansh','bardoli',567554845],[5,'raj','mp',54643845]]
w.writerows(rows)

#five records taken input from user. 
l=[]
for i in range(5):
    a=int(input("enter student id:"))
    b=input("enter student name:")
    c=input("enter city:")
    d=int(input("enter contect number:"))
    la=[a,b,c,d]
    l.append(la)
w.writerows(l)
q.close()

#Read this file using csv module and print it. 
from csv import DictReader
with open('c:\\22bca221\\python\\student2.csv','r',newline='')as p:
    m=DictReader(p)
    for row in m:
        print(row)
