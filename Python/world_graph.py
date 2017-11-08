import pandas as pd
import pygal as pg
import math
from pygal.style import Style
from pygal.style import NeonStyle

def worldgraph():
    start = int(input())
    stop = int(input())
    #----Read CSV----#
    df_world = pd.read_csv("../DATA/Total population.csv", encoding = "UTF-8")
    df_world.index = df_world['Country Name']


    #----Adding years pop----#
    years = []
    for i in range(start, stop+1):
        total = 0
        for j in df_world[str(i)]:
            if math.isnan(j) is True:
                continue
            total += j
        years += [total]


    #----Pygal----#
    country_rawpop = pg.StackedLine(fill=True, style=NeonStyle, width = 2000)
    country_rawpop.x_labels = map(str, [str(i) for i in range(start, stop+1)])
    country_rawpop.add("Year:", years)
    country_rawpop.render_to_file('Graph SVG/World_Graph.svg')
worldgraph()
