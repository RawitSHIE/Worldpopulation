import pandas as pd
import pygal as pg
from pygal.style import Style
def main():
    """pop indicator"""

    #----input----#
    Country = input()
    year = input()


#----------------------------------------------------------------------------------#

    #-----read file-----#
    df_male = pd.read_csv("../DATA/Male/Male Total Population.csv", encoding = "UTF-8")
    df_female = pd.read_csv("../DATA/Female/Female_Total_Population.csv", encoding = "UTF-8")


#----read CSV----#
    df_fe = []
    df_ma = []
    for i in range(0, 80+1, 5):
        df_ma += [pd.read_csv("../DATA/Male/male age {0}-{1}.csv".format(i, i+4), encoding = "UTF-8")]
        df_fe += [pd.read_csv("../DATA/Female/Female age {0}-{1}.csv".format(i, i+4), encoding = "UTF-8")]


#----set index----#
    df_female.index = df_male['Country Name']
    df_male.index = df_male['Country Name']
    for i in range(len(df_ma)):
        df_ma[i].index = df_ma[i]['Country Name']
        df_fe[i].index = df_fe[i]['Country Name']


#----collect pop----#
    male_age = []
    male_total = df_male.loc[Country,year]

    female_age = []
    female_total = df_female.loc[Country,year]
    
    for i in range(len(df_ma)):
        male_age += [df_ma[i].loc[Country, year]/100 *male_total]
        female_age += [df_fe[i].loc[Country, year]/100 *female_total]

#----------------------------------------------------------------------------------#

#---- Sutract DATA----#
    male_age = [int(x) for x in male_age]
    female_age = [int(y) for y in female_age]
    total_age = [int(x)+int(y) for x, y in zip(male_age, female_age)]
    bar = ["Age 0-4","Age 5-9","Age 10-14","Age 15-19","Age 20-24","Age 25-29",\
          "Age 30-34","Age 35-39","Age 40-44","Age 45-49","Age 50-54","Age 55-59",\
          "Age 60-64","Age 65-69","Age 70-74","Age 75-79","Age 80++"]

#----pygal----#

    custom_style = Style(
        background='Black',
        plot_background='Black',
        foreground='White',
        foreground_strong='White',
        foreground_subtle='#630C0D',
        opacity='.6',
        transition='400ms ease-in',
        colors=('#0090F1',  '#E89B53')
        )
    bar_chartboth = pg.HorizontalStackedBar(interpolate='cubic', style=custom_style)
    bar_chartboth.x_labels = map(str, bar)
    bar_chartboth.add("Male", male_age)
    bar_chartboth.add("Female", female_age)
    bar_chartboth.render_to_file('Graph SVG/Range_both_en.svg')
main()