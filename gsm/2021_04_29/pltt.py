import matplotlib. pyplot as plt
x=[x for x in range(-10,10)]
y1=[2*t for t in x]
y2=[t**2 + 5 for t in x]
y3= [-t**2 -5 for t in x]
plt.plot(x,y1,'r--',label="y1=2x")
plt.text(0,0,'y1=2x')
plt.plot(x,y2,"g^-",label='y2=x**2+5')
plt.plot(x,y3,'b*:',label='y3-x**2-5')

plt.axis([-20,20,-20,20])
plt.legend()
plt.show()