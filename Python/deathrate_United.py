import pandas as pd
import pygal

def death():
    death_sheet = pd.read_csv("..\DATA\Deathrate\Deathrate.csv", encoding = 'UTF-8')
    death_sheet.index = death_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    colors=('#FF0000', '#f1be54', '#76FC00', '#3280ee'),
    )
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, width=1000, x_label_rotation=90)
    line_chart.title = 'Deathrate of United States'
    line_chart.x_labels = map(str, range(1960, 2016))
    line_chart.value_formatter = lambda x: "%.2f" %x + "%"
    line_chart.add('United States', death_sheet.loc["United States"][4:60])
    line_chart.render_to_file('Graph SVG/Deathrate of United States.svg')
death()
