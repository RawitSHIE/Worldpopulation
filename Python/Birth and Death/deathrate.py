import pandas as pd
import pygal

def death():
    #----Read CSV----#
    death_sheet = pd.read_csv("C:/Users/USER/Desktop/PSIT/Worldpopulation/DATA/Deathrate/Deathrate.csv", encoding = 'UTF-8')
    death_sheet.index = death_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    colors=('#FF0000', '#f1be54', '#76FC00', '#3280ee'),
    )
    #----add to line chart----#
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, width=1000, x_label_rotation=90)
    line_chart.title = 'Deathrate (in %)'
    line_chart.x_labels = map(str, range(1960, 2016))
    line_chart.value_formatter = lambda x: "%.2f" %x + "%"
    line_chart.add('China', death_sheet.loc["China"][4:60])
    line_chart.add('Thailand', death_sheet.loc["Thailand"][4:60])
    line_chart.add('Japan', death_sheet.loc["Japan"][4:60])
    line_chart.add('United States', death_sheet.loc["United States"][4:60])
    line_chart.render_to_file('C:/Users/USER/Desktop/PSIT/Worldpopulation/Python/Graph SVG/Deathrate.svg')
death()
