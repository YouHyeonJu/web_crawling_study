import matplotlib.pyplot as plt
fig, ax= plt.subplots(2,2,figsize=(7,7))

x=[x for x in range(10)]
y1= [2*t for t in x]
y2=[t**2+5 for t in x]
y3= [-t**2 -5 for t in x]
y4=[-t for t in x]

ax[0,0].plot(x,y1,'r--')
ax[0,0].text(0,0,'y1=2x',fontsize=10)
ax[0,1].plot(x,y2,'b*-')
ax[1,0].plot(x,y3,'g^-')
ax[1,1].plot(x,y4,'yellowgreen')

plt.show()