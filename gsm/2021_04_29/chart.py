import re
import numpy as np
txt='abc@facebook.com 와 bbc@google.com에서 이메일이 도착하였습니다.'
# output=re.findall('\S+@[a-z.]+',txt)
# print("추출된 이메일: ",output)
# output=re.findall('\w+@[a-z.]+',txt)
# print("추출된 이메일: ",output)
output=re.findall('\S+@[a-z.]+',txt)
for text in output:
    text_split=text.split('@')
    print("추출된 아이디"+text_split[0]+"도메인:"+text_split[1])

y=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
np_y= np.array(y)
print(np_y)
print(np_y[0:2,2:4])
print(np_y[::2,::2])
print(np_y[1::2,1::2])

players= [[170,76.4],[183,86.2],[181,78.5],[176,80.1]]

np_players=np.array(players)
print("몸무게가 80 이상인 선수 정보")
print(np_players[np_players[:,1]>=80.0])

print("키가 180이상인 선수 정보")
print(np_players[np_players[:,0]>=180.0])