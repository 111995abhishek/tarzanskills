#s="my name is varun and my phone number is +919739921787"
#for x in s:
 #   if x.isdigit():
  #      print(x)
#s="my name is varun
# my email id is varun.rathore@gmail.com"
 # ""
#import re
#phone_number="my number is +91 9739921787"
#razex=re.compile(r"(\+[\d]{2}+)([\d]+)")
#matches=razex.search(phone_number)
#print(matches.group())
#import re
#phone_number="my no is 9739921787 varun no is 1234567890 and piyush no is 9876543210"
#razex=re.compile(r"[\w\d{10}]+")
#matches=razex.findall(phone_number)
#print(*matches,sep='\n')
import re
password=input()
razex=re.compile(r"[a-z]+")
razex1=re.compile(r"[A-z]+")

