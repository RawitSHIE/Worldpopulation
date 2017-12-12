"""PopEachContry"""
import pandas as pd
import pygal
def worldpop():
    total_csv = pd.read_csv("../../DATA/Total population.csv", encoding = "UTF-8")
    country = input()
    step = int(input())
    pop_list = list()
    years_list = list()
    hav = False

    for name in range(len(total_csv['Country Name'])):
        if total_csv['Country Name'][name] == country:
            hav = True
            for year in range(1960, 2017, step):
                pop_list.append(int(total_csv[str(year)][name]))

    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    		colors=('#0000FF', '#FF0000')
    		)
    if hav:
        from pygal.style import NeonStyle

        line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, x_label_rotation=90)
        line_chart.title = "Thailand Year: 1960 - 2016 AD"
        line_chart.x_labels = [str(i) for i in range(1960, 2017, step)]
        line_chart.value_formatter = lambda x: "{:,} People".format(x)
        line_chart.add('Populations', pop_list)
        line_chart.render_to_file('../Graph SVG/pop_bar_chart.svg')  
        print(*pop_list)
    else:
        print('not Found')
worldpop()
