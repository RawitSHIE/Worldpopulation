import pandas as pd
import pygal as pg
from pygal.style import NeonStyle
def rangeage():
    """pop indicator"""

    #----input----#
    Country = input()
#----------------------------------------------------------------------------------#

    #-----read file-----#
    df_male = pd.read_csv("../../../../DATA/Male/Male Total Population.csv", encoding = "UTF-8")
    df_female = pd.read_csv("../../../../DATA/Female/Female Total Population.csv", encoding = "UTF-8")


#----read CSV----#
    df_fe = []
    df_ma = []
    for i in range(0, 80+1, 5):
        df_ma += [pd.read_csv("../../../../DATA/Male/male age {0}-{1}.csv".format(i, i+4), encoding = "UTF-8")]
        df_fe += [pd.read_csv("../../../../DATA/Female/Female age {0}-{1}.csv".format(i, i+4), encoding = "UTF-8")]


#----set index----#
    df_female.index = df_male['Country Name']
    df_male.index = df_male['Country Name']
    for i in range(len(df_ma)):
        df_ma[i].index = df_ma[i]['Country Name']
        df_fe[i].index = df_fe[i]['Country Name']


#----collect pop----#
    for y in range(1960, 2017):
        str_y = str(y)
        male_age = []
        male_total = df_male.loc[Country,str_y]

        female_age = []
        female_total = df_female.loc[Country,str_y]
        
        for i in range(len(df_ma)):
            male_age += [df_ma[i].loc[Country, str_y]/100 *male_total]
            female_age += [df_fe[i].loc[Country, str_y]/100 *female_total]

#----------------------------------------------------------------------------------#

#---- Sutract DATA----#
        male_age = [int(x) for x in male_age]
        female_age = [int(y) for y in female_age]
        total_age = [int(x)+int(y) for x, y in zip(male_age, female_age)]
        bar = ["Age 0-4","Age 5-9","Age 10-14","Age 15-19","Age 20-24","Age 25-29",\
            "Age 30-34","Age 35-39","Age 40-44","Age 45-49","Age 50-54","Age 55-59",\
            "Age 60-64","Age 65-69","Age 70-74","Age 75-79","Age 80++"]

#----pygal----#
        age_pyramid = pg.Pyramid(interpolate='cubic', style=NeonStyle, x_label_rotation=90)
        age_pyramid.x_labels = map(str, bar)
        age_pyramid.value_formatter = lambda x: "{:,}".format(int(x))
        age_pyramid.title = 'Age Seperation: Population of {0} AD ({1})'.format(y, Country)
        age_pyramid.add("Male", male_age)
        age_pyramid.add("Female", female_age)
        age_pyramid.render_to_file('usa_range/usa_range_{0}.svg'.format(y))
        print(male_age, female_age)
rangeage()
