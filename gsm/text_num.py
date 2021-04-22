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
f= open("Data/UNDHR.txt")
for line in f:
    if re.search("^\([0-9]+\)",line):
        print(line)