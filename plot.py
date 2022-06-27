import matplotlib.pyplot as plt
from numpy import square
plt.style.available

plt.style.use('seaborn')
fig,ax = plt.subplots()
#ax.plot(x_value,squares,linewidth = 3)
ax.set_title("My plot",fontsize = 20)
ax.set_xlabel("X",fontsize = 14)
ax.set_ylabel("Y",fontsize = 14)
ax.tick_params(axis='both',labelsize=14)

x_val = range(1,1001)
y_val = [x**2 for x in x_val]
ax.scatter(x_val,y_val,c = y_val,cmap=plt.cm.Blues,s=10)
ax.axis([0,1100,0,1100000])
plt.show()
