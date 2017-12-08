import pandas as pd
import pygal

def birth():
    birth_sheet = pd.read_csv("..\DATA\Birthrate\Birthrate.csv", encoding = 'UTF-8')
    birth_sheet.index = birth_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    colors=('#FF0000', '#f1be54', '#76FC00', '#3280ee'),
    )
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, width=1000, x_label_rotation=90)
    line_chart.title = 'Birthrate of Thailand'
    line_chart.x_labels = map(str, range(1960, 2016))
    line_chart.value_formatter = lambda x: "%.2f" %x + "%"
    line_chart.add('Thailand', birth_sheet.loc["Thailand"][4:60])
    line_chart.render_to_file('Graph SVG/Birthrate of Thailand.svg')
birth()
