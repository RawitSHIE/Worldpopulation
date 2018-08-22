import pandas as pd
import pygal as pg
import math
from pygal.style import Style
from pygal import Config

def worldgraph():
    start = int(input())
    stop = int(input())
    step = 1
    #----Read CSV----#
    df_world = pd.read_csv("../DATA Update/Total population.csv", encoding = "UTF-8")
    df_world.index = df_world['Country Name']
    
    #----Adding years pop----#
    years = []
    for i in range(start, stop+1, step):
        years += [df_world.loc["World", str(i)]]


    #----Pygal----#
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
        background="transparent"
    )
    country_rawpop = pg.StackedLine(fill=True, style=NeonStyle, x_label_rotation=90, x_labels_major_every= check(start, stop), human_readable = True, width=1000 )
    country_rawpop.x_labels = map(str, [str(i) for i in range(start, stop+1, step)])
    # country_rawpop.y_value_formatter = lambda x:  "%.2f Million" % (x / 1000000)
    country_rawpop.value_formatter = lambda x: "{:,} People".format(x)
    country_rawpop.title = 'World Populations'
    country_rawpop.add("Year:", years)
    country_rawpop.render_to_file('Graph SVG/World_Graph.svg')


def check(x, y):
    """check"""
    if y-x <= 15:
        return 1
    else:
        for i in range(1, y-x):
            if (y-x)%i >= 10:
                return i
worldgraph()
