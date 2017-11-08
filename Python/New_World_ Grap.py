import pandas as pd
import pygal as pg
import math
from pygal.style import Style
import numpy as np
#############################################################################################################################################################################################################################
def column_index(df, query_cols):
    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols,query_cols,sorter=sidx)]
#############################################################################################################################################################################################################################
def main():
    year = input()
    df_world = pd.read_csv("../DATA/fixed index total.csv", encoding = "UTF-8")
    df_world.index = df_world['Country Name']
    reg = {v:0 for v in set(df_world['Country Code'])}
#############################################################################################################################################################################################################################
    for idx, val in enumerate(df_world.values):
        col = column_index(df_world, year)
        i = val[0]
        if i not in ["World", "East Asia & Pacific (excluding high income)", "Early-demographic dividend", "East Asia & Pacific", "Europe & Central Asia (excluding high income)","Europe & Central Asia"\
    "World", "High income", "Low income", "Lower middle income", "Low & middle income",\
     "Middle East & North Africa", "Middle East & North Africa (excluding high income)",\
      "Other small states", "Post-demographic dividend",\
       "Latin America & the Caribbean (IDA & IBRD countries)",\
        "Middle East & North Africa (IDA & IBRD countries)", "Middle income",\
         "Upper middle income", "East Asia & Pacific (IDA & IBRD countries)",\
          "Europe & Central Asia (IDA & IBRD countries)", "South Asia (IDA & IBRD)",\
           "European Union", "Fragile and conflict affected situations",\
            "Heavily indebted poor countries (HIPC)", "IBRD only", "IDA & IBRD total",\
             "IDA total", "IDA blend", "IDA only", "Late-demographic dividend", "North America",\
              "OECD members", "Pacific island small states", "Sub-Saharan Africa (excluding high income)",\
               "Latin America & the Caribbean (IDA & IBRD countries)", "Sub-Saharan Africa (IDA & IBRD countries)"]:
            print(idx)
            reg[val[1]] += df_world.iloc[idx, col] if not math.isnan(df_world.iloc[idx, col]) else 0
#############################################################################################################################################################################################################################
    custom_style = Style(
                    background='Black',
                    plot_background='Black',
                    foreground='White',
                    foreground_strong='White',
                    foreground_subtle='#630C0D',
                    opacity='.6',
                    transition='100ms ease-in',
                    colors=('#E853A0',  '#E8537A')
                    )
#############################################################################################################################################################################################################################
    worldmap_chart = pg.maps.world.World()
    worldmap_chart.title = 'World Popultaion in any years'
    worldmap_chart.add('In {}'.format(year), reg)
    worldmap_chart.render_to_file('Graph SVG/World_Map.svg') 
main()
