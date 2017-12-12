import pandas as pd
import pygal

def birth():
    #----Receive input----#
    country = input()
    #----Read CSV----#
    birth_sheet = pd.read_csv("C:/Users/USER/Desktop/PSIT/Worldpopulation/DATA/Birthrate/Birthrate.csv", encoding = 'UTF-8')
    birth_sheet.index = birth_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    colors=('#FF0000', '#f1be54', '#76FC00', '#3280ee'),
    )
    #----add to line chart----#
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, width=1000, x_label_rotation=90)
    line_chart.title = 'Birthrate of ' + country
    line_chart.x_labels = map(str, range(1960, 2016))
    line_chart.value_formatter = lambda x: "%.2f" %x + "%"
    line_chart.add(country, birth_sheet.loc[country][4:60])
    line_chart.render_to_file('C:/Users/USER/Desktop/PSIT/Worldpopulation/Python/Graph SVG/Birthrate of {0}.svg'.format(country))
birth()
