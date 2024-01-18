# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:59:36 2023

@author: jorge
"""

#Import pandas
import pandas as pd

# Open en read "country_wise_latest.csv"
covid = pd.read_csv("C:/Users/jorge/Documents/Anaconda files/country_wise_latest.csv")

#Check de dataframe met head() en info()
print("=============COVID Dataset==============")
print(covid.head())
print(covid.info())

#Clean Data
#Check voor non_values
print(covid.isna().sum())
if covid.isna().sum().any : 0
print("=============COVID Dataset is schoon==============")

#Import plotly
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'

#Figure1: "Recovered cases vs Deaths cases per WHO Region"
#Isoleer de variabels dat je wilt analyseren
print("=============Recovered cases vs Deaths cases per WHO Region==============")
covid_rvsd = covid[['Country/Region', 'Recovered', 'Deaths', 'WHO Region']].sort_values(by=['Recovered'], ascending=False)
covid_rvsd["Difference"] = covid_rvsd['Recovered'] - covid_rvsd['Deaths']
print(covid_rvsd.head())

#Zet de variabels in een plot
fig1 = px.scatter(data_frame=covid_rvsd, x='Recovered', 
                 y='Deaths', 
                 color='WHO Region',
                 symbol="WHO Region",
                 title="Recovered COVID cases vs Death COVID cases per WHO Region",
                 hover_name='Country/Region',
                 hover_data='Difference',
                 trendline='ols',
                 trendline_scope='overall')

#Schrijft je "annotations" en "legend"
my_annotations = {'x': 1325804, 
                  'y': 148011,
                  'showarrow': True,'arrowhead': 5,
                  'text': "US have a lot of recovered cases, but also a lot of death cases ",
                  'font' : {'size': 15, 'color': 'black'}}
my_legend = {'bgcolor': 'rgb(70, 200, 201)', 'borderwidth': 1}

#Update de layout van de figure
fig1.update_layout({'annotations': [my_annotations]})

fig1.update_layout({'showlegend': True, 'legend': my_legend})

fig1.update_layout({'xaxis': {'title': {'text':"Recovered Cases"}},
                  'yaxis': {'title': {'text':"Death Cases"}}})

fig1.update_layout({'xaxis': {'range': [-10000, covid_rvsd['Recovered'].max() + 25000]}})

fig1.update_layout({'yaxis': {'range': [-10000, covid_rvsd['Deaths'].max() + 25000]}})

#Laat figure 1 zien
fig1.show() 

#Figure 2: "Confirmed cases from last week per WHO Region"
#Isoleer de variabels dat je wilt analyseren
print("=============Confirmed cases from last week in America vs Confirmed cases from last week in Europa==============")
covid_lw = covid[['Country/Region', 'Confirmed last week', 'WHO Region']].sort_values(by=['Confirmed last week'], ascending=False)
print(covid_lw.head())

#Zet de variabels in een plot
fig2 = px.bar(data_frame=covid_lw, x="WHO Region",
                    y='Confirmed last week',
                    title="Confirmed COVID cases from last week per WHO Region ",
                    color='WHO Region',
                    hover_name="Country/Region")

#Schrijft je "annotations" en "legend"
my_annotations2 = {'x': 'Americas', 
                  'y': 7815198,
                  'showarrow': True,'arrowhead': 5,
                  'text': " The Americas region have the more confirmed cases in the last week",
                  'font' : {'size': 15, 'color': 'black'}}

my_legend2 = {'bgcolor': 'rgb(70, 200, 201)', 'borderwidth': 1}

#Update de layout van de figure
fig2.update_layout({'annotations': [my_annotations2]})

fig2.update_layout({'showlegend': True, 'legend': my_legend2})

fig2.update_layout({'xaxis': {'title': {'text':"WHO Region"}},
                  'yaxis': {'title': {'text':"Cases confirmed last week"}}})

fig2.show()
 

