import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = "sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index, colum_header in enumerate(header_row):
       # print(index,colum_header)
    dates=[]
    highs=[]
    lows=[]

    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
    #print(highs)
    plt.style.use('classic')
    fig,ax = plt.subplots()
    ax.plot(dates,highs,c='red')
    ax.plot(dates,lows,c='blue')
    ax.set_title("Daily high tmp, July 2018",fontsize = 24)
    ax.set_xlabel('',fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("F",fontsize=16)
    ax.tick_params(axis='both',which='major',labelsize=12)
    plt.show()