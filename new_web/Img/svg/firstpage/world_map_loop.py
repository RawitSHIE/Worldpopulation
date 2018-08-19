import pandas as pd
import pygal as pg
import math
import numpy as np
from utils import check_path
check_path("Graph SVG")
#############################################################################################################################################################################################################################
def column_index(df, query_cols):
    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols,query_cols,sorter=sidx)]
#############################################################################################################################################################################################################################
def main(year):
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
            
            reg[val[1]] += df_world.iloc[idx, col] if not math.isnan(df_world.iloc[idx, col]) else 0
#############################################################################################################################################################################################################################
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
            height=1200,
            background='transparent',
            plot_background='transparent',
            colors=('#66ccff', '#FF0000')
            )
#############################################################################################################################################################################################################################
    worldmap_chart = pg.maps.world.World(fill=True, interpolate='cubic', style=NeonStyle)
    worldmap_chart.title = 'World Populations Map ({0} AD)'.format(year)
    worldmap_chart.add('In {}'.format(year), reg)
    worldmap_chart.render_to_file('Graph SVG/world_map/world_map_{0}.svg'.format(year))
    print(year)
def recur():
    for i in range(1960, 2017):
       main(str(i))
recur()
