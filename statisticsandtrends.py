# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 04:47:32 2022

@author: LENOVO 
"""
#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#function to read the file
def read_fle(finame):
    '''
    

    Parameters
    ----------
    finame : csv file

    Returns
    -------
    dt :dataframe with years as columns
    dttranspose : dataframe with countries as columns

    '''
    
    dt = pd.read_csv(finame)
    #transposing the file
    dttranspose= dt.set_index('Country Name').transpose()
    return dt, dttranspose
#taking the list of countries   
count1= ['Argentina','China','Denmark','United Kingdom','India','Malaysia']
count2= ['Belgium','Spain','Greece','Italy','Malta','Nepal']

#filtering the data to plot bardata
def bar_filter_data(dt):
    """
    

    Parameters
    ----------
    dt : dataframe with years as columns

    Returns
    -------
    dt : filtered data to plot bardata

    """
    dt=dt[['Country Name','Indicator Name','2000','2005','2010','2015','2019']]
    dt = dt [(dt["Country Name"]=="Argentina") | 
                 (dt["Country Name"]=="China") | 
                 (dt["Country Name"]=="Denmark") |
                 (dt["Country Name"]=="United Kingdom") | 
                 (dt["Country Name"]=="India") |
                 (dt["Country Name"]=="Malaysia")]
    return dt

#filtering the data to plot linedata
def line_filter_data(dt):
    dt=dt[['Country Name','Indicator Name','2000','2005','2010','2015','2019']]
    dt =dt [(dt["Country Name"]=="Belgium") | 
                (dt["Country Name"]=="Spain") | 
                (dt["Country Name"]=="Greece") |
                (dt["Country Name"]=="Italy") |
                (dt["Country Name"]=="Malta") | 
                (dt["Country Name"]=="Nepal")]
    return dt

#function to plot bargraph    
def bar_plot(dt, lbl1, lbl2):
    plt.figure(figsize=(35,20))
    axx= plt.subplot(1,1,1)
    x = np.arange(6)
    width= 0.2
    bar1= axx.bar(x, dt["2000"],width,label= 2000)
    bar2= axx.bar(x+width, dt["2005"], width, label=2015)
    bar3= axx.bar(x+width*2, dt["2015"], width, label=2019)
    
    axx.set_xlabel("Name of Country", fontsize= 45)
    axx.set_ylabel(lbl1, fontsize= 50)
    axx.set_title(lbl2, fontsize=50)
    axx.set_xticks(x, count1, fontsize=30, rotation=90)
    axx.legend(fontsize=30)
             
    axx.bar_label(bar1, padding=2, rotation=90, fontsize= 17)
    axx.bar_label(bar2, padding=2, rotation=90, fontsize= 17)
    axx.bar_label(bar3, padding=2, rotation=90, fontsize= 17)
    plt.savefig("Barplots.png")
    plt.show()    

#function to plot linegraph     
def line_plot(dt,lbl1,lbl2):
    plt.figure(figsize=(15,10))
    d = dt.set_index('Country Name')
    transp = d.transpose()
    transp = transp.drop(index=['Indicator Name'])
    for i in range(len(count2)):
        plt.plot(transp.index, transp[count2[i]], label=count2[i])
        
    plt.title(lbl2, size=25)
    plt.xlabel("Years", size=20)
    plt.ylabel(lbl1, size=20)
    plt.xticks(rotation=90)
    plt.legend(fontsize=11)
    plt.savefig("LinePlots.png")
    plt.show()

#reading the 1st file             
pop_dt, pop_dt1 = read_fle("C:/Users/LENOVO/Desktop/Assignment2/Population.csv")
pop_dt = bar_filter_data(pop_dt)
#reading the 2nd file       
Agr_dt, Agr_dt1 = read_fle("C:/Users/LENOVO/Desktop/Assignment2/Agricultures.csv") 
Agr_dt = bar_filter_data(Agr_dt)

#reading the 3rd file       
CO2_dt, CO2_dta1=read_fle("C:/Users/LENOVO/Desktop/Assignment2/Co2.csv")   
CO2_dt= line_filter_data(CO2_dt)
#reading the 4th file       
NO2_dt, No2_dta1 = read_fle("C:/Users/LENOVO/Desktop/Assignment2/Nitrousoxide.csv")             
NO2_dt= line_filter_data(NO2_dt)          

bar_plot(pop_dt, "Population(Total)","Total Population")
bar_plot(Agr_dt, 'Agricultural land(% of land','Agricultural land(sq.km)') 

line_plot(CO2_dt,"CO2 Emission(KT)","CO2 Emission (KT)")
line_plot(NO2_dt,"Nitrous oxide emission(%)","NO2 emission")

#function to find the mean
def No2_emission_mean():
    
    
    """
    

    Returns
    -------
    Meandata: dataframe with average of No2 emissions of 4 countries

    """
    #reading the dataframes from No2 emission data
    dt,ttranspose = read_fle("C:/Users/LENOVO/Desktop/Assignment2/Nitrousoxide.csv")
    data = dt.set_index('Country Name')
    
    dtrans=data.transpose()
    dtrans = dtrans.drop(index='Indicator Name')
    dtrans = dtrans.drop(index='Indicator Code')
    dtrans = dtrans.drop(index='Country Code')
    #replacing the NaN values
    clean_data = dtrans.fillna(0)
    meandata = clean_data[["Argentina","China","Denmark","India"]].mean()
    
    return meandata
#calling the function   
meandata= No2_emission_mean()
meandata = meandata.to_csv("meanno2.csv")
