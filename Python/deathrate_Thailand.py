import pandas as pd
import pygal

def death():
    death_sheet = pd.read_csv("../DATA Update/Deathrate/death.csv", encoding = 'UTF-8')
    death_sheet.index = death_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    colors=('#FF0000', '#f1be54', '#76FC00', '#3280ee'),
    )
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, width=1000, x_label_rotation=90)
    line_chart.title = 'Deathrate of Thailand'
    line_chart.x_labels = map(str, range(1960, 2017))
    line_chart.value_formatter = lambda x: "%.2f" %x + "%"
    line_chart.add('Thailand', death_sheet.loc["Thailand"][4:61])
    line_chart.render_to_file('Graph SVG/Deathrate of Thailand.svg')
death()
