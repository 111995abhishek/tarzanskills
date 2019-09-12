spam=['apple','banana','tofu','cat']
new_spam=""
for i in spam:
    if i== spam[-1]:
        new_spam= new_spam +' and '
        new_spam= new_spam+i
    else:
        new_spam= new_spam + i +","
print("'"+new_spam+"'")

