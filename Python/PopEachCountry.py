"""PopEachContry"""
import pandas as pd
import pygal
def worldpop():
    total_csv = pd.read_csv("../DATA/Total population.csv", encoding = "UTF-8")
    country = input()
    years1 = int(input())
    years2 = int(input())
    pop_list = list()
    years_list = list()
    hav = False

    for name in range(len(total_csv['Country Name'])):
        if total_csv['Country Name'][name] == country:
            hav = True
            for year in range(years1, years2+1):
                pop_list.append(int(total_csv[str(year)][name]))

    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    		colors=('#0000FF', '#FF0000')
    		)
    if hav:

        line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle)
        line_chart.title = country
        line_chart.x_labels = range(years1, years2+1)
        line_chart.add('Populaions', pop_list)
        line_chart.render_to_file('Graph SVG/pop_bar_chart.svg')  
        print(*pop_list)
    else:
        print('not Found')
worldpop()