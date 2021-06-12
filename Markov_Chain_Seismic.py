# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:59:28 2021

@author: Aleksander Kudyba i Bartosz Szych

-wstępna analiza danych;
-wyznaczenie prawdopodobieństw przejć między stanami na podstawie danych
-symulacja jednego roku 
-ustalenie zbieżnoci wyników
"""

import numpy as np

def get_data():
    df=np.loadtxt('2016-2020.csv', dtype=str, delimiter=',')
    return df
df = get_data()

"""
ANALIZA DANYCH
"""

no_tremor = []
tremor = []
tremor_trace = []
tremor_light = []
tremor_medium = []
tremor_strong = []
tremor_very_strong = []

transContainer00 = []
transContainer01 = [] # dla 0 do RG
transContainer02 = [] # dla 0 do RZ
transContainer03 = [] # dla 0 do RP
transContainer11 = [] #z RG do RG
transContainer22 = [] #z RZ do RZ
transContainer33 = [] #z RP do RP
transContainer10 = [] #z RG do 0
transContainer12 = [] #z RG do RZ
transContainer13 = [] #z RG do RP
transContainer20 = [] #z RZ do 0
transContainer21 = [] #z RZ do RG
transContainer23 = [] #z RZ do RP
transContainer30 = [] #z RP do 0
transContainer31 = [] #z RP do RG
transContainer32 = [] #z RP do RZ

stateSpace = ['none','trace','light','medium','strong','veryStrong']

for i in range (2,len(df)):
    if int(df[i-1][6])==0 and int(df[i-1][7])==0 and int(df[i-1][8])==0 and int(df[i][6])==0 and int(df[i][7])==0 and int(df[i][8])==0:
        transContainer00.append(1)
        
    elif int(df[i-1][6])==0 and int(df[i-1][7])==0 and int(df[i-1][8])==0 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i][9] == 'RG':
        transContainer01.append(1)
        
    elif int(df[i-1][6])==0 and int(df[i-1][7])==0 and int(df[i-1][8])==0 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i][9] == 'RZ':
        transContainer02.append(1)
        
    elif int(df[i-1][6])==0 and int(df[i-1][7])==0 and int(df[i-1][8])==0 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i][9] == 'RP':
        transContainer03.append(1)
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RG' and df[i][9] == 'RG':
        transContainer11.append(1)
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RZ' and df[i][9] == 'RZ':
        transContainer22.append(1)
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RP' and df[i][9] == 'RP':
        transContainer33.append(1)
        
    elif int(df[i][6])==0 and int(df[i][7])==0 and int(df[i][8])==0 and float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and df[i-1][9] == 'RG':
        transContainer10.append(1) 
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RG' and df[i][9] == 'RZ':
        transContainer12.append(1)  
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RG' and df[i][9] == 'RP':
        transContainer13.append(1)  
        
    elif int(df[i][6])==0 and int(df[i][7])==0 and int(df[i][8])==0 and float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and df[i-1][9] == 'RZ':
        transContainer20.append(1)    
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RZ' and df[i][9] == 'RG':
        transContainer21.append(1)
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RZ' and df[i][9] == 'RP':
        transContainer21.append(1) 
        
    elif int(df[i][6])==0 and int(df[i][7])==0 and int(df[i][8])==0 and float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and df[i-1][9] == 'RP':
        transContainer30.append(1)    

    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RP' and df[i][9] == 'RG':
        transContainer31.append(1) 
        
    elif float(df[i-1][5]) > 0 and  float(df[i-1][5]) < 1e7 and float(df[i][5]) > 0 and  float(df[i][5]) < 1e7 and df[i-1][9] == 'RP' and df[i][9] == 'RZ':
        transContainer32.append(1)    


for i in range(1,len(df)):
    if int(df[i][6])==0 and int(df[i][7])==0 and int(df[i][8])==0:
        no_tremor.append(1)
    elif float(df[i][5]) > 0 and  float(df[i][5]) < 1e3:
        tremor_trace.append(1)
    elif float(df[i][5]) < 1e4:
        tremor_light.append(1)
    elif float(df[i][5]) < 1e5:
        tremor_medium.append(1)
    elif float(df[i][5]) < 1e7:
        tremor_strong.append(1)
    else: 
        tremor_very_strong.append(1)

frequencies = [(len(no_tremor)*100)/len(df), (len(tremor_trace)*100)/len(df),(len(tremor_light)*100)/len(df),(len(tremor_medium)*100)/len(df),(len(tremor_strong)*100)/len(df),(len(tremor_very_strong)*100)/len(df)] 
print(frequencies,sum(frequencies))

"""
SYMULACJA
"""


# The statespace
states = ["Brak wstrząsu", "Wstrząs w RG", "Wstrząs w RZ", "Wstrząs w RP"]  # 0, 1, 2, 3 

# Possible sequences of events
transitionName = [["00","01","02", "03"],["10","11","12", "13"],["20","21","22","23"],["30","31","32","33"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.9165,0.0478,0.0250,0.0107],[0.2729,0.6951,0.0227,0.0093],[0.5518,0.0545,0.3937,0], [0.6849,0.0383,0.0306,0.2462]] #changed from the base example

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[2])+sum(transitionMatrix[3]) != 4:
    print("Sums of probabilieties in transitoin matrix don't add up to 1. Correct the transition matrix.")
else: print("Transition matrix initialized correctly.")

"""
input: number of cycles i.e. Markov chain steps
output: list of predicted states during the number of MC steps = 17520 (average time between measurements = 0.5 h)
"""
def states_forecast(steps):
    startingState = "Brak wstrząsu"
    stateList = [startingState]
    
    i = 0 #enumerator for the while loop
    prob = 1
    while i < steps:
        if startingState == "Brak wstrząsu":
            """
    From transitionName space random.choice chooses 
    by sampling probability distribution of transitionMatrix (p) for the corresponding
    transitionName space, the next state  
    """
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
    #now, to update the activity list
            if change == "00":
                prob = prob * 0.9165
                stateList.append("Brak wstrząsu")
                pass
            elif change == "01":
                prob = prob * 0.0478
                stateList.append("Wstrząs w RG")
            elif change == "02":
                prob = prob * 0.0250
                stateList.append("Wstrząs w RZ")
            else:
                prob = prob * 0.0107
                stateList.append("Wstrząs w RP")
        elif startingState == "Wstrząs w RG":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "10":
                prob = prob * 0.2729
                stateList.append("Brak wstrząsu")
            elif change == "11":
                prob = prob * 0.6951
                stateList.append("Wstrząs w RG")
            elif change == "12":
                prob = prob * 0.0227
                stateList.append("Wstrząs w RZ")
            else:
                prob = prob * 0.0093
                stateList.append("Wstrząs w RP")
        elif startingState == "Wstrząs w RZ":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "20":
                prob = prob * 0.5518
                stateList.append("Brak wstrząsu")
            elif change == "21":
                prob = prob * 0.0545
                stateList.append("Wstrząs w RG")
            elif change == "22":
                prob = prob * 0.03937
                stateList.append("Wstrząs w RZ")
            else:
                prob = prob * 0
                stateList.append("Wstrząs w RP")
        elif startingState == "Wstrząs w RP":
            change = np.random.choice(transitionName[3],replace=True,p=transitionMatrix[3])
            if change == "30":
                prob = prob * 0.6849
                stateList.append("Brak wstrząsu")
            elif change == "31":
                prob = prob * 0.0383
                stateList.append("Wstrząs w RG")
            elif change == "32":
                prob = prob * 0.0306
                stateList.append("Wstrząs w RZ")
            else:
                prob = prob * 0.2462
                stateList.append("Wstrząs w RP")
        i+=1
    return stateList




prob1 = []
prob2 = []
prob3 = []
prob4 = []

brakCount = 0
brakCount1 = 0
brakCount2 = 0
brakCount3 = 0
brakCount4 = 0

RGcount = 0
RGCount1 = 0
RGCount2 = 0
RGCount3 = 0
RGCount4 = 0

RZcount = 0
RZCount1 = 0
RZCount2 = 0
RZCount3 = 0
RZCount4 = 0

RPcount = 0 
RPCount1 = 0
RPCount2 = 0
RPCount3 = 0
RPCount4 = 0 

for j in range(1,501):
    oneYearPrediction = states_forecast(17520)   # dla tego okresu będziemy musieli policzyć zbieżnoć występowań stanów
  
    for i in range(len(oneYearPrediction)):
        if oneYearPrediction[i] == "Brak wstrząsu":
            brakCount += 1
            if i < len(oneYearPrediction)*0.25:
                brakCount1 += 1
            elif i >= len(oneYearPrediction)*0.25 and i < len(oneYearPrediction)*0.5:
                brakCount2 += 1
            elif i >= len(oneYearPrediction)*0.5 and i < len(oneYearPrediction)*0.75:
                brakCount3 += 1
            else:
                brakCount4 += 1
        elif oneYearPrediction[i] == "Wstrząs w RG":
            RGcount += 1
            if i < len(oneYearPrediction)*0.25:
                RGCount1 += 1
            elif i >= len(oneYearPrediction)*0.25 and i < len(oneYearPrediction)*0.5:
                RGCount2 += 1
            elif i >= len(oneYearPrediction)*0.5 and i < len(oneYearPrediction)*0.75:
                RGCount3 += 1
            else:
                RGCount4 += 1
        elif oneYearPrediction[i] == "Wstrząs w RZ":
            RZcount += 1
            if i < len(oneYearPrediction)*0.25:
                RZCount1 += 1
            elif i >= len(oneYearPrediction)*0.25 and i < len(oneYearPrediction)*0.5:
                RZCount2 += 1
            elif i >= len(oneYearPrediction)*0.5 and i < len(oneYearPrediction)*0.75:
                RZCount3 += 1
            else:
                RZCount4 += 1
        elif oneYearPrediction[i] == "Wstrząs w RP":
            RPcount += 1
            if i < len(oneYearPrediction)*0.25:
                RPCount1 += 1
            elif i >= len(oneYearPrediction)*0.25 and i < len(oneYearPrediction)*0.5:
                RPCount2 += 1
            elif i >= len(oneYearPrediction)*0.5 and i < len(oneYearPrediction)*0.75:
                RPCount3 += 1
            else:
                RPCount4 += 1
                
                
       
    
    prob1.append(brakCount/j/len(oneYearPrediction))
    prob2.append(RGcount/j/len(oneYearPrediction))
    prob3.append(RZcount/j/len(oneYearPrediction))
    prob4.append(RPcount/j/len(oneYearPrediction))

brakCount1 = int(brakCount1/j)
brakCount2 = int(brakCount2/j)
brakCount3 = int(brakCount3/j)
brakCount4 = int(brakCount4/j)     

RGCount1 = int(RGCount1/j)
RGCount2 = int(RGCount2/j)
RGCount3 = int(RGCount3/j)
RGCount4 = int(RGCount4/j)  

RZCount1 = int(RZCount1/j)
RZCount2 = int(RZCount2/j)
RZCount3 = int(RZCount3/j)
RZCount4 = int(RZCount4/j)  

RPCount1 = int(RPCount1/j)
RPCount2 = int(RPCount2/j)
RPCount3 = int(RPCount3/j)
RPCount4 = int(RPCount4/j)    

layer = [[RGCount1,RGCount2,RGCount3,RGCount4],[RZCount1,RZCount2,RZCount3,RZCount4],[RPCount1,RPCount2,RPCount3,RPCount4]]        
bins = ['Q1','Q2','Q3','Q4']



import matplotlib.pyplot as plt
data = layer
X = ['Q1','Q2','Q3','Q4']
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X, data[0], color = 'b', width = 0.25)
ax.bar(X, data[1], color = 'g', width = 0.25)
ax.bar(X, data[2], color = 'r', width = 0.25)
ax.legend(labels=['wstrząsy w RG','wstrząsy w RZ','wstrząsy w RP'])




fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Qs = ['Q1','Q2','Q3','Q4']
czysto = [brakCount1,brakCount2,brakCount3,brakCount4]
ax.bar(Qs,czysto)
plt.show()
# plt.plot(prob1)
# plt.plot(prob2) 
# plt.plot(prob3) 
# plt.plot(prob4)        
                
           
                
                
                
                
                
                
                
                
                