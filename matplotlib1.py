

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,4,5]
"""plt.plot(x,y)
#plt.show()
plt.plot(x,y,'b.')#ro, g^, r--, b-, b--
#plt.show()
plt.plot(x,y)
plt.axis([0,10,0,200])
#plt.show()
plt.plot(x,y,'r--',label="Y=X",linewidth=1)
plt.axis([0,5,0,5])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("X vs Y")
plt.legend()
#plt.show()
plt.plot([1,2,3,4,5],[1,2,4,8,16],'r--',label="Y=2**(X-1)",linewidth=1)
plt.plot([1,2,3,4,5],[3,9,27,81,273],'b--',label="Y=3**(X)",linewidth=1)
plt.axis([0,10,0,300])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("X vs Y")
plt.show()"""

plt.bar([1,2,3,4,5],[20,40,60,80,100],color='r')
plt.bar([1,2,3,4,5],[2,4,6,8,10],color='b')
plt.bar(["1","Female Literacy"],[120,60])
plt.show()
