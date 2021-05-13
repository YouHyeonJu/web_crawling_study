import re
# print(re.search("A..A",'ABA'))
# print(re.search("A..A",'ABBA'))
# print(re.search("A..A",'ABBA'))

# print(re.search("AB*",'A'))
# print(re.search("AB*",'AA'))
# print(re.search("AB*",'HOPE'))
# print(re.search("AB*",'X-MAN'))
# print(re.search("AB*",'CABBA'))
# print(re.search("AB*",'CABBBBBA'))

# print(re.search("AB?",'A'))
# print(re.search("AB?",'AA'))
# print(re.search("AB?",'J-HOPE'))
# print(re.search("AB?",'X-MAN'))
# print(re.search("AB?",'CABBA'))
# print(re.search("AB?",'CABBBBBA'))

# print(re.search("AB+",'A'))
# print(re.search("AB+",'AA'))
# print(re.search("AB+",'J-HOPE'))
# print(re.search("AB+",'X-MAN'))
# print(re.search("AB+",'CABBA'))
# print(re.search("AB+",'CABBBBBA'))

# txt_1="My life my life my life in the sunshine"
# print(re.findall("[Mm]y",txt_1))
# text="""101 COM PythonProgramming 102 MAT LinearAlgebra 103 ENG ComputerEnglish"""
# s=re.findall('\d+',text)
# print(s)
# f= open("Data/UNDHR.txt")
# for line in f:
#     if re.search("^\([0-9]+\)",line):
#         print(line)
txt='abc@facebook.com 와 bbc@google.com에서 이메일이 도착하였습니다.'
# output=re.findall('\S+@[a-z.]+',txt)
# print("추출된 이메일: ",output)
# output=re.findall('\w+@[a-z.]+',txt)
# print("추출된 이메일: ",output)
output=re.findall('\S+@[a-z.]+',txt)
for text in output:
    text_split=text.split('@')
    print("추출된 아이디"+text_split[0]+"도메인:"+text_split[1])

s="My lucky number 27 99"
print(re.sub("[0-9]+","*",s))
print(re.sub('\d+','*',s))

st="{'locs': [(128, 139, 262, 295)], 'preds': array([[0.03960581, 0.96039414]], dtype=float32)}"
print(re.sub('\w\w\w\w','*',st))