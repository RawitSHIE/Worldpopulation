import pandas as pd
import pygal as pg
import math
from pygal.style import Style

def main():
    start = int(input())
    stop = int(input())
    df_world = pd.read_csv("../DATA/Total population.csv", encoding = "UTF-8")
    df_world.index = df_world['Country Name']
    years = []
    for i in range(start, stop+1):
        total = 0
        for j in df_world[str(i)]:
            if math.isnan(j) is True:
                continue
            total += j
        years += [total]

    custom_style = Style(
                    background='Black',
                    plot_background='Black',
                    foreground='White',
                    foreground_strong='White',
                    foreground_subtle='#630C0D',
                    opacity='.6',
                    transition='100ms ease-in',
                    colors=('#0090F1',  '#E89B53')
                    )
    country_rawpop = pg.StackedLine(fill=True, style=custom_style)
    country_rawpop.x_labels = map(str, [str(i) for i in range(start, stop+1)])
    country_rawpop.add("Year:", years)
    country_rawpop.render_to_file('Graph SVG/World_Graph.svg')
main()
