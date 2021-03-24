# def Sumof_odd_even():
#     a=[x for x in range(100) if x%2==0]
#     print("짝수: ",sum(a))
#     b=[x for x in range(100) if x%2!=0]
#     print("홀수: ",sum(b))
# Sumof_odd_even()
# import random
# a=[]
# for x in range(10):
#     n = random.randrange(100)
#     a.append(n)
# print(a)
# a.reverse()
# print(a)
# f= open(filename,'r',encoding='utf-8')
# for i in f:
#     print(i.strip())
# f.close()
# with open (filename,'r',encoding='utf-8') as f:
#     for i in f:
#         print(i.strip())

# f.write("동해물과 백두산이 마르고 닭 도록 하느님이 보우하사 우리나라만세\n")
# f.write("무 궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세\n")
# f.close()
# temp = '\t\t\n\n apple \n\n\t\t'
# print(temp)
# print('[{}]'.format(temp))
#
#
# t= temp.strip()
# print('[{}]'.format(t))
# print(t)
#
# a='AA,BB,CC,DD'
# print(a.split(','))
# b= a.split(',')
#
# c='***'.join(b)
# print(c)
#
#
# a=list(range(1,16,2))
# print(a)

filename='Data2/poem2.txt'
f=open(filename,'r',encoding='utf-8')
for i in f:
    print(i.strip())
f.close()


