import matplotlib.pyplot as plt

from random_walk import Randomwalk
while(True):
  rw = Randomwalk()
  rw.fill_walk()
  plt.style.use('classic')
  fig,ax = plt.subplots()
  ax.scatter(rw.x_val,rw.y_val,s=15)
  plt.show()
  keep_running = input("continue? y/n\n ")
  if keep_running == 'n':
      break


    
