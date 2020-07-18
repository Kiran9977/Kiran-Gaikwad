import urllib.request as request
import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime

d=False
while not d:
        try:
                date_entry = input('Enter a start date from data u want date in YYYY-MM-DD format:')
                year, month, day = map(int, date_entry.split('-'))
                Sdate = datetime.date(year, month, day)

                date_entry2 = input('Enter a end date upto data u want date in YYYY-MM-DD format:')
                year1, month1, day1 = map(int, date_entry2.split('-'))
                Edate = datetime.date(year1, month1, day1)
                d=True

        except:
                print("wrong entry")

isValid=False
while not isValid:
	a=input("enter 1st valid symbol:")
	b=input("enter 2st valid symbol:")
	try:
                with request.urlopen('https://api.exchangeratesapi.io/history?start_at={2}&end_at={3}&symbols={0},{1}'.format(a,b,Sdate,Edate)) as response:

                    source = response.read()
                    data1 = json.loads(source)
                    isValid=True
	except:
		        print ("try again!\n")


df=pd.DataFrame(data1['rates'])

x=[]
y=[]
date=[]

for row in df:
	date.append(row)

df1=df.transpose()

x=df1[a].tolist()
y=df1[b].tolist()

plt.plot(date,x, label=a)
plt.plot(date,y, label=b)
plt.ylabel('Y')
plt.xlabel('date')
plt.title('Exchange Rate Against EUR')
plt.legend()
plt.show()