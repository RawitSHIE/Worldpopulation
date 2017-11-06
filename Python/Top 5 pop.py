import pandas as pd
import pygal as pg
from pygal.style import Style
import math


def main():
    year = input()
    df_world = pd.read_csv("../DATA/Total population.csv", encoding = "UTF-8")
    df_world.index = df_world['Country Name']
    dict_con = {}
    for i in df_world['Country Name']:
        if i == "World"\
        or i == "East Asia & Pacific (excluding high income)"\
        or i == "Early-demographic dividend"\
        or i == "East Asia & Pacific"\
        or i == "Europe & Central Asia (excluding high income)"\
        or i == "Europe & Central Asia"\
        or i == "World"\
        or i == "High income"\
        or i == "Low income"\
        or i == "Lower middle income"\
        or i == "Low & middle income"\
        or i == "Middle East & North Africa"\
        or i == "Middle East & North Africa (excluding high income)"\
        or i == "Other small states"\
        or i == "Post-demographic dividend"\
        or i == "Latin America & the Caribbean (IDA & IBRD countries)"\
        or i == "Middle East & North Africa (IDA & IBRD countries)"\
        or i == "Middle income"\
        or i == "Upper middle income"\
        or i == "East Asia & Pacific (IDA & IBRD countries)"\
        or i == "Europe & Central Asia (IDA & IBRD countries)"\
        or i == "South Asia (IDA & IBRD)"\
        or i == "European Union"\
        or i == "Fragile and conflict affected situations"\
        or i == "Heavily indebted poor countries (HIPC)"\
        or i == "IBRD only"\
        or i == "IDA & IBRD total"\
        or i == "IDA total"\
        or i == "IDA blend"\
        or i == "IDA only"\
        or i == "Late-demographic dividend"\
        or i == "North America"\
        or i == "OECD members"\
        or i == "Pacific island small states"\
        or i == "Sub-Saharan Africa (excluding high income)"\
        or i == "Latin America & the Caribbean (IDA & IBRD countries)"\
        or i == "Sub-Saharan Africa (IDA & IBRD countries)"\
        or math.isnan(df_world.loc[i, year]) is True:
            continue

        dict_con[i] = df_world.loc[i, year]
    sort_high = sorted(dict_con.values())[-1:-5:-1]
    print(sort_high)
main()
