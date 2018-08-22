import pandas as pd
import pygal as pg
from pygal.style import Style
import math


def main():
    df_world = pd.read_csv("../DATA Update/Total population.csv", encoding = "UTF-8")
    df_world.index = df_world['Country Name']
    dict_con = {}
    restrict = ["World"\
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
    , 'Sub-Saharan Africa']
    for k in range(1960,2018):
        m = str(k)
        for i in df_world['Country Name']:
            if i in restrict\
            or math.isnan(df_world.loc[i, m]):
                continue

            dict_con[i] = df_world.loc[i, m]

        sort_high = sorted(dict_con, key=dict_con.__getitem__)[-1:-6:-1]
        sort_high_val = [dict_con[i] for i in sort_high]

        print(sort_high)
        print(sort_high_val)
        from pygal.style import NeonStyle
        NeonStyle = NeonStyle(
                colors=('#5555FF', '#550000')
                )
        bar_chartboth = pg.Bar(interpolate='cubic', style=NeonStyle)
        bar_chartboth.title = 'Top 5 highest population (year:{0})'.format(k)
        bar_chartboth.value_formatter = lambda x: "{:,} People".format(x)
        bar_chartboth.x_labels = map(str, sort_high)
        bar_chartboth.add("Population", sort_high_val)
        bar_chartboth.render_to_file('Graph SVG/top_5/top_{0}.svg'.format(k))
main()
