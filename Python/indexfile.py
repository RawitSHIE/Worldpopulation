
import pandas as pd
import math
import pygal as pg
import webbrowser
def main():
    df_world = pd.read_csv("../DATA Update/Total population.csv", encoding = "UTF-8")
    df_world.index = df_world['Country Name']
    for i in df_world['Country Name'][:5]:
        if i in ["World"\
        , "East Asia & Pacific (excluding high income)"\
        , "Early-demographic dividend"\
        , "East Asia & Pacific"\
        , "Europe & Central Asia (excluding high income)"\
        , "Europe & Central Asia"\
        , "World"\
        , "High income"\
        , "Low income"\
        , "Lower middle income"\
        , "Low & middle income"\
        , "Middle East & North Africa"\
        , "Middle East & North Africa (excluding high income)"\
        , "Other small states"\
        , "Post-demographic dividend"\
        , "Latin America & the Caribbean (IDA & IBRD countries)"\
        , "Middle East & North Africa (IDA & IBRD countries)"\
        , "Middle income"\
        , "Upper middle income"\
        , "East Asia & Pacific (IDA & IBRD countries)"\
        , "Europe & Central Asia (IDA & IBRD countries)"\
        , "South Asia (IDA & IBRD)"\
        , "European Union"\
        , "Fragile and conflict affected situations"\
        , "Heavily indebted poor countries (HIPC)"\
        , "IBRD only"\
        , "IDA & IBRD total"\
        , "IDA total"\
        , "IDA blend"\
        , "IDA only"\
        , "Late-demographic dividend"\
        , "North America"\
        , "OECD members"\
        , "Pacific island small states"\
        , "Sub-Saharan Africa (excluding high income)"\
        , "Latin America & the Caribbean (IDA & IBRD countries)"\
        , "Sub-Saharan Africa (IDA & IBRD countries)"\
        , 'South Asia'\
        , 'Euro area'\
        , 'Least developed countries: UN classification'\
        , 'Latin America & Caribbean (excluding high income)'\
        , "Pre-demographic dividend"\
        , "Latin America & Caribbean"\
        , "Arab World"\
        , 'Sub-Saharan Africa']:
            continue
        new = 2
        taburl = "https://en.wikipedia.org/wiki/";
        term = i;
        webbrowser.open(tabUrl+term, new=new)
main()
