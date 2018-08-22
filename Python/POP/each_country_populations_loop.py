"""PopEachContry"""
import pandas as pd
import pygal
import math
def worldpop(country, step):
    total_csv = pd.read_csv("../../DATA Update/Total population.csv", encoding = "UTF-8")
    total_csv.index = total_csv["Country Name"]
    pop_list = list()
    years_list = list()
    hav = False
    for year in range(1960, 2017, step):
        if math.isnan(total_csv.loc[country, str(year)]):
            pop_list = []
            print(country)
            break
        pop_list.append(total_csv.loc[country, str(year)])

    from pygal.style import NeonStyle

    if not hav:
        from pygal.style import NeonStyle
        NeonStyle = NeonStyle(
        background='transparent',
        colors=('#0000FF', '#FF0000')
        )
        line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, x_label_rotation=90, width=1000)
        line_chart.title = "{} Year: 1960 - 2016 AD".format(country)
        line_chart.x_labels = [str(i) for i in range(1960, 2017, step)]
        line_chart.value_formatter = lambda x: "{:,} People".format(x)
        line_chart.add('Populations', pop_list)
        line_chart.render_to_file('../Graph SVG/each_pop/pop_bar_{}.svg'.format(country))
        print(*pop_list)
    else:
        print('not Found')


def recur():
    step = int(input())
    df = pd.read_csv("../../DATA Update/Total population.csv", encoding = "UTF-8")
    for i in df['Country Name']:
        worldpop(i, step)
recur()
