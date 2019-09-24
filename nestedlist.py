#n=int(input())
#for i in range(n)
 #   name=input()
  #  score=float(input())
#cd
students = []
marks = []
num = input("How many students?:  ")
for i in num:
     name = input("input name of student "+ i)
     students.append(name)
     mark = input("input mark of the student")
     marks.append(mark)
for i in num:
     print(students[i] + ": "  ,marks[i])

