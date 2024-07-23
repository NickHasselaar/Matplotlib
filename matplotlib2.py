import matplotlib.pyplot as plt
"""ages=[13,68,23,41,29,92,84,23,1,18,70,30]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins,histtype="bar",rwidth=0.8)
plt.xlabel("age")
plt.ylabel("bins")
plt.show()
x=[1,4,9,8,2]
y=[3,9,1,5,4]
plt.scatter(x,y,label="scatterplot",color="green",marker="X")
plt.show()
slices=[23,40,35,2]
activities=["hockey","football","volleyball","basketball"]
a=["r","c","g","b","y"]
plt.pie(slices,labels=activities,colors=a,startangle=190,shadow=True)
plt.show()"""
days=[0,1,2,3,4]
hockey=[5,20,12,19,12]
football=[1,2,1,3,1]
volleyball=[3,10,9,8,4]
basketball=[30,29,39,28,42]
plt.plot([],[],color="red",label="hockey",linewidth=1)
plt.plot([],[],color="blue",label="football",linewidth=1)
plt.plot([],[],color="green",label="volleyball",linewidth=1)
plt.plot([],[],color="yellow",label="basketball",linewidth=1)
plt.stackplot(days,hockey,football,volleyball,basketball,colors=["red","blue","green","yellow"])
plt.show()
#plt.subplot(221) - the cooncerned subplot, 2 - total row, 2 - total column, 1 - index in the subplot matrix