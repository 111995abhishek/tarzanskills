#integers=[1,2,3,4,5,6,1]
#for i in integers:

   # if integers[0]==integers[-1]:
#original_list= [11, 45, 8, 11, 23, 45, 23, 45, 89]
#for i in original_list:
 #   occur = original_list.count(i)
  #  print(occur)
#duplicate_list=[]
#duplicate_list.append()

#COUNTING OCCURENCE OF ELEMENT IN LIST AND PUTTING INTO DICTIONARY
initial_list=[11,45,8,11,23,45,23,45,89]
final_dict={}
for i in initial_list:
    count=0
    for j in initial_list:
        if i == j:
            count = count + 1
    final_dict[i]=count
print(final_dict)









# EXERCISE PROBLEM
#spam=['apples','banana','tofu','cats']
#def convert(spam):
 #   final_string = ""
  #  for i in spam:

   # print('',final_string)
#spam.insert(-1,'and')
#print(spam)
#def listToString(spam):
 #   str1 = " "

  #  return (str1.join(spam))
#spam = ['apple','banana','tofu','cats']
#print(listToString(spam))
#def(list)










