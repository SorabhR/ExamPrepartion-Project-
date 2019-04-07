
import pandas as pd
import datetime

#import data csv file
df = pd.read_csv('Automatic email content store.csv',sep = "$")

#removing invalid date 
df['Date'] = pd.to_datetime(df['Date'], dayfirst = True,format = "%d/%m/%y",errors='coerce')
df.dropna(axis=0,inplace=True)

#for all unique email address
unique = []
unique = df['to '].unique()
unique.sort()
#print(unique)

#for last conversation date
last_convo =[]
for i in range(0,len(unique)):
    last_convo.append(max(df['Date'].loc[df['to ']==unique[i]]))

for i in range(0,len(last_convo)):
    last_convo[i] = last_convo[i].date()

#time elapse since last conversation
def time_elapsed_calculator(last_convo):
    today = datetime.datetime.now().date()
    time_elapsed = []
    for i in range(0,len(last_convo)):
        time_elapsed.append((today-last_convo[i]))
    return time_elapsed

time_elapsed = time_elapsed_calculator(last_convo)
for i in range(0,len(time_elapsed)):
    time_elapsed[i] = time_elapsed[i].days

#print days elapsed
for i in range(0,len(time_elapsed)):
    print("The last conversation with %s was %s days back"%(unique[i],time_elapsed[i]))
    

#function to search words
for i in range(len(df)):
    df['keyword'] = "no keyword"

def search(keyword):
    flag = 0
    for i in range(len(df)):
        if(keyword.lower() in (df['raw'].iloc[i]).lower()):
            flag = 1
            if(df['keyword'].iloc[i] == "no keyword"):
                df['keyword'].iloc[i] = keyword
            else:
                df['keyword'].iloc[i] = ("%s , %s"%(df['keyword'].iloc[i],keyword))
    if (flag==0):
        print("The searched agrument was not found")
    else:
        print("The searched agrument was found")

search_array = ["OpenCv","Python"]
for x in search_array:
    search(x)

        