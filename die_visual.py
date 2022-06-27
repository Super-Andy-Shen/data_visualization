from plotly.graph_objs import Bar,Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()
results = []

for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies =[]
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
x_val = list(range(1,max_result + 1))
data = [Bar(x = x_val,y = frequencies)]

x_aixs_config = {'title':'Result','dtick':1}
y_aixs_config = {'title':'Frequency of Result'}
my_layout = Layout(title='Result of 10000 times',xaxis=x_aixs_config,yaxis=y_aixs_config)
offline.plot({'data':data,'layout':my_layout},filename='andy.html')



