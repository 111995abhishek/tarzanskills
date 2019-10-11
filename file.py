#file=open("test.txt","r")
#print(file.read())
#file.close()

#with open("test.txt","r") as file:
 #   print(file.read())

#with open("hello.txt","r") as content:
#    print(content.readlines())


#content=open("hello.txt","r")
#for line in content:
 #   print(line)
#content.close()

#content=open("hello.txt","r")
#for line in content:
 #   print(line,end='')
#content.close()

#file=open("hello.txt","r")
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')
#content=file.readline()
#print(content,end='')


#with open("hello.txt","r") as f:
 #   for line in f:
  #      print(line,end='')


#with open("hello.txt","r") as f:
#    content=f.read(10)
 #   print(content)

#with open("hello.txt","r") as f:
 #   content=f.readline(10)
  #  print(content)
   # content = f.readline(10)
    #print(content)
    #content = f.readline(10)
    #print(content)
    #content = f.readline(10)
    #print(content)


#with open("hello.txt","r") as f:
 #   content=f.read(5)
  #  print(content)
   # content = f.read(5)
    #print(content)
    #content = f.read(5)
    #print(content)
   # content = f.read(5)
   # print(content)


#with open("hello.txt","r") as f:
 #   f.seek(0)
  #  content=f.read(10)
   # print(content)



#with open("hello.txt","r") as file:
#    size=10
 #   content=file.read(size)
  #  while len(content)>0:
   #     print(content,end='**')
    #    content=file.read(size)


#with open("varun.txt","w") as file:
  #  file.write("hello")

#with open("varun.txt","w") as file:
 #   file.write("test")
  #  file.seek(0)
   # file.write("r")


#with open("index.jpeg","rb") as rf:
    #with open("varun.jpeg","wb") as wf:
        #for line in rf:
           # wf.write(line)



#with open("varun.jpeg","rb") as rf:
 #   with open("tarzanskills.png","wb") as wf:
  #      chunk_size=4096
   #     rf_chunk=rf.read(chunk_size)
    #    while len(rf_chunk)>0:
     #       wf.write(rf_chunk)
      #      rf_chunk=rf.read(chunk_size)
dict_inventory={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
for keys,values in dict_inventory:
    print()