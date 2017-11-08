import pandas as pd
import pygal as pg
from pygal.style import Style
def main():
    """pop indicator"""

    #input
    Country = input()
    year = input()


#----------------------------------------------------------------------------------#



    #read file male
    df_male = pd.read_csv("../DATA/Male/Male Total Population.csv", encoding = "UTF-8")
    df_male00_04 = pd.read_csv("../DATA/Male/male age 0-4.csv", encoding = "UTF-8")
    df_male05_09 = pd.read_csv("../DATA/Male/male age 5-9.csv", encoding = "UTF-8")
    df_male10_14 = pd.read_csv("../DATA/Male/male age 10-14.csv", encoding = "UTF-8")
    df_male15_19 = pd.read_csv("../DATA/Male/male age 15-19.csv", encoding = "UTF-8")
    df_male20_24 = pd.read_csv("../DATA/Male/male age 20-24.csv", encoding = "UTF-8")
    df_male25_29 = pd.read_csv("../DATA/Male/male age 25-29.csv", encoding = "UTF-8")
    df_male30_34 = pd.read_csv("../DATA/Male/male age 30-34.csv", encoding = "UTF-8")
    df_male35_39 = pd.read_csv("../DATA/Male/male age 35-39.csv", encoding = "UTF-8")
    df_male40_44 = pd.read_csv("../DATA/Male/male age 40-44.csv", encoding = "UTF-8")
    df_male45_49 = pd.read_csv("../DATA/Male/male age 45-49.csv", encoding = "UTF-8")
    df_male50_54 = pd.read_csv("../DATA/Male/male age 50-54.csv", encoding = "UTF-8")
    df_male55_59 = pd.read_csv("../DATA/Male/male age 55-59.csv", encoding = "UTF-8")
    df_male60_64 = pd.read_csv("../DATA/Male/male age 60-64.csv", encoding = "UTF-8")
    df_male65_69 = pd.read_csv("../DATA/Male/male age 65-69.csv", encoding = "UTF-8")
    df_male70_74 = pd.read_csv("../DATA/Male/male age 70-74.csv", encoding = "UTF-8")
    df_male75_79 = pd.read_csv("../DATA/Male/male age 75-79.csv", encoding = "UTF-8")
    df_male80 = pd.read_csv("../DATA/Male/male age 80up.csv", encoding = "UTF-8")

    #read file female
    df_female = pd.read_csv("../DATA/Female/Female_Total_Population.csv", encoding = "UTF-8")
    df_female00_04 = pd.read_csv("../DATA/Female/Female age 0-4.csv", encoding = "UTF-8")
    df_female05_09 = pd.read_csv("../DATA/Female/Female age 5-9.csv", encoding = "UTF-8")
    df_female10_14 = pd.read_csv("../DATA/Female/Female age 10-14.csv", encoding = "UTF-8")
    df_female15_19 = pd.read_csv("../DATA/Female/Female age 15-19.csv", encoding = "UTF-8")
    df_female20_24 = pd.read_csv("../DATA/Female/Female age 20-24.csv", encoding = "UTF-8")
    df_female25_29 = pd.read_csv("../DATA/Female/Female age 25-29.csv", encoding = "UTF-8")
    df_female30_34 = pd.read_csv("../DATA/Female/Female age 30-34.csv", encoding = "UTF-8")
    df_female35_39 = pd.read_csv("../DATA/Female/Female age 35-39.csv", encoding = "UTF-8")
    df_female40_44 = pd.read_csv("../DATA/Female/Female age 40-44.csv", encoding = "UTF-8")
    df_female45_49 = pd.read_csv("../DATA/Female/Female age 45-49.csv", encoding = "UTF-8")
    df_female50_54 = pd.read_csv("../DATA/Female/Female age 50-54.csv", encoding = "UTF-8")
    df_female55_59 = pd.read_csv("../DATA/Female/Female age 55-59.csv", encoding = "UTF-8")
    df_female60_64 = pd.read_csv("../DATA/Female/Female age 60-64.csv", encoding = "UTF-8")
    df_female65_69 = pd.read_csv("../DATA/Female/Female age 65-69.csv", encoding = "UTF-8")
    df_female70_74 = pd.read_csv("../DATA/Female/Female age 70-74.csv", encoding = "UTF-8")
    df_female75_79 = pd.read_csv("../DATA/Female/Female age 75-79.csv", encoding = "UTF-8")
    df_female80 = pd.read_csv("../DATA/Female/Female age 80+.csv", encoding = "UTF-8")

#set index
    #----male----#
    df_male.index = df_male['Country Name']
    df_male00_04.index = df_male00_04['Country Name']
    df_male05_09.index =df_male05_09['Country Name']
    df_male10_14.index =df_male10_14['Country Name']
    df_male15_19.index =df_male15_19['Country Name']
    df_male20_24.index =df_male20_24['Country Name']
    df_male25_29.index =df_male25_29['Country Name']
    df_male30_34.index =df_male30_34['Country Name']
    df_male35_39.index =df_male35_39['Country Name']
    df_male40_44.index =df_male40_44['Country Name']
    df_male45_49.index =df_male45_49['Country Name']
    df_male50_54.index =df_male50_54['Country Name']
    df_male55_59.index =df_male55_59['Country Name']
    df_male60_64.index =df_male60_64['Country Name']
    df_male65_69.index =df_male65_69['Country Name']
    df_male70_74.index =df_male70_74['Country Name']
    df_male75_79.index =df_male75_79['Country Name']
    df_male80.index =   df_male80['Country Name']


    #----female----#
    df_female.index = df_male['Country Name']
    df_female00_04.index = df_male00_04['Country Name']
    df_female05_09.index = df_female05_09['Country Name']
    df_female10_14.index = df_female10_14['Country Name']
    df_female15_19.index = df_female15_19['Country Name']
    df_female20_24.index = df_female20_24['Country Name']
    df_female25_29.index = df_female25_29['Country Name']
    df_female30_34.index = df_female30_34['Country Name']
    df_female35_39.index = df_female35_39['Country Name']
    df_female40_44.index = df_female40_44['Country Name']
    df_female45_49.index = df_female45_49['Country Name']
    df_female50_54.index = df_female50_54['Country Name']
    df_female55_59.index = df_female55_59['Country Name']
    df_female60_64.index = df_female60_64['Country Name']
    df_female65_69.index = df_female65_69['Country Name']
    df_female70_74.index = df_female70_74['Country Name']
    df_female75_79.index = df_female75_79['Country Name']
    df_female80.index =    df_female80['Country Name']




#------------------convert perentage to int num------------------------#
    #----range male----#
    male_age = []
    male_total = df_male.loc[Country,year]
    male_age.append(df_male00_04.loc[Country, year]/100 *male_total)
    male_age.append(df_male05_09.loc[Country, year]/100 *male_total)
    male_age.append(df_male10_14.loc[Country, year]/100 *male_total)
    male_age.append(df_male15_19.loc[Country, year]/100 *male_total)
    male_age.append(df_male20_24.loc[Country, year]/100 *male_total)
    male_age.append(df_male25_29.loc[Country, year]/100 *male_total)
    male_age.append(df_male30_34.loc[Country, year]/100 *male_total)
    male_age.append(df_male35_39.loc[Country, year]/100 *male_total)
    male_age.append(df_male40_44.loc[Country, year]/100 *male_total)
    male_age.append(df_male45_49.loc[Country, year]/100 *male_total)
    male_age.append(df_male50_54.loc[Country, year]/100 *male_total)
    male_age.append(df_male55_59.loc[Country, year]/100 *male_total)
    male_age.append(df_male60_64.loc[Country, year]/100 *male_total)
    male_age.append(df_male65_69.loc[Country, year]/100 *male_total)
    male_age.append(df_male70_74.loc[Country, year]/100 *male_total)
    male_age.append(df_male75_79.loc[Country, year]/100 *male_total)
    male_age.append(df_male80.loc[Country, year]/100 *male_total)


    #----range female----#
    female_age = []
    female_total = df_female.loc[Country,year]
    female_age.append(df_female00_04.loc[Country, year]/100 *female_total)
    female_age.append(df_female05_09.loc[Country, year]/100 *female_total)
    female_age.append(df_female10_14.loc[Country, year]/100 *female_total) 
    female_age.append(df_female15_19.loc[Country, year]/100 *female_total)
    female_age.append(df_female20_24.loc[Country, year]/100 *female_total)
    female_age.append(df_female25_29.loc[Country, year]/100 *female_total)
    female_age.append(df_female30_34.loc[Country, year]/100 *female_total)
    female_age.append(df_female35_39.loc[Country, year]/100 *female_total)
    female_age.append(df_female40_44.loc[Country, year]/100 *female_total)
    female_age.append(df_female45_49.loc[Country, year]/100 *female_total)
    female_age.append(df_female50_54.loc[Country, year]/100 *female_total)
    female_age.append(df_female55_59.loc[Country, year]/100 *female_total)
    female_age.append(df_female60_64.loc[Country, year]/100 *female_total)
    female_age.append(df_female65_69.loc[Country, year]/100 *female_total)
    female_age.append(df_female70_74.loc[Country, year]/100 *female_total)
    female_age.append(df_female75_79.loc[Country, year]/100 *female_total)
    female_age.append(df_female80.loc[Country, year]/100 *female_total)

#----------------------------------------------------------------------------------#

#---- Sutract DATA----#
    male_age = [int(x) for x in male_age]
    female_age = [int(y) for y in female_age]
    total_age = [int(x)+int(y) for x, y in zip(male_age, female_age)]
    bar = ["Age 0-4","Age 5-9","Age 10-14","Age 15-19","Age 20-24","Age 25-29",\
          "Age 30-34","Age 35-39","Age 40-44","Age 45-49","Age 50-54","Age 55-59",\
          "Age 60-64","Age 65-69","Age 70-74","Age 75-79","Age 80++"]




    #----test output----#
    #print(bar)
    #print(total_age)


#----pygal----#

    #bar_chart = pg.HorizontalStackedBar()
    #bar_chart.add("age", total_age)
    #bar_chart.render_to_file('Graph SVG/Range_age.svg')

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
    bar_chartboth.render_to_file('Graph SVG/Range_both.svg')

main()