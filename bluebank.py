# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:32:47 2025

@author: Shinjini Banerjee
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#method1 to reaad json data

json_file=open('loan_data_json.json')
data=json.load(json_file)

lists=['apple','banana','pear']

#append

lists.append('cherry')

#insert iteminto aspecific position

lists.insert(1,'grape')
print(lists)

#changeitemsin a list

lists.remove('apple')
print(lists)

lists.pop()

print(lists)

#workingwith dictionaries

#transform to data frame
loandata=pd.DataFrame(data)

#finding unique values 
loandata['purpose'].unique()

#describig the data

loandata.describe()
loandata['int.rate'].describe()
loandata['int.rate'].describe()
loandata['dti'].describe()

#using exp to get the annualincome
income=np.exp(loandata['log.annual.inc'])
loandata['annualincome']=income
loandata=loandata.drop('annual_income',axis=1)

#zero D  arrays
arr=np.array(43)
arr=np.array([1,2,3,4])
arr=np.array([[1,2,3],[4,5,6]])

#working with if 

#ficoscore

fico=250

if fico>=300 and fico<400:
    ficocat='very poor'
elif fico>=400 and fico<600:
    ficocat='poor'
elif fico>=601 and fico<660:
    ficocat='fair'
elif fico>=660 and fico<700:
    ficocat='good'
elif fico>=700:
    ficocat='excellent'
else:
    ficocat='unknown'
    print(ficocat)

#forloops
length=len(loandata)
ficocat=[]
for x in range(0,length):
    category=loandata['fico'][x]
   

   
    ficocat.append(cat)     
    
ficocat=pd.Series(ficocat)
       
loandata['fico.category']= ficocat

i=10
while i<100:
    print(i)
    i=i+1
    
length=len(loandata)
ficocat=[]
for x in range(0,length):
    category='red'
   
    try:
        if category>=3 and category<400:
            cat='very poor'
        elif category>=400 and category<600:
             cat='poor'
        elif category>=601 and category<660:
             cat='fair'
        elif category>=660 and category<700:
             cat='good'
        elif category>=700:
             cat='excellent'
        else:
             ficocat='unknown'
    except:
        cat='error-unnknown'
ficocat.append(cat)
        
ficocat=pd.Series(ficocat)
       
loandata['fico.category']= ficocat

length=len(loandata)
ficocat=[]
for x in range(0,length):
    category=loandata['fico'][x]
    if category>=3 and category<400:
        cat='very poor'
    elif category>=400 and category<600:
         cat='poor'
    elif category>=601 and category<660:
         cat='fair'
    elif category>=660 and category<700:
         cat='good'
    elif category>=700:
         cat='excellent'
    else:
         ficocat='unknown'
    ficocat.append(cat)
    
ficocat=pd.Series(ficocat)
       
loandata['fico.category']= ficocat

#dfloc for interest rates 

loandata.loc[loandata['int.rate']>0.12,'int.rate.type']='high'
loandata.loc[loandata['int.rate']<=0.12,'int.rate.type']='low'

#plotting charts


#numberof loans by fico catrgory

catplot=loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green',width=0.1)
plt.show()
purplot=loandata.groupby(['purpose']).size()
purplot.plot.bar(color='purple',width=0.2)
plt.show()

#scatterplot dti and annual income
ypoint=loandata['annualincome']
xpoint=loandata['dti']
plt.scatter(xpoint,ypoint,color='#4caf50')
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index=True)
