"""
GNI for CN, TH, JP, USA
"""
import pandas as pd
import pygal

def gni():
    gdp_sheet = pd.read_csv("..\DATA\gni\gni.csv", encoding = 'UTF-8')
    gdp_sheet.index = gdp_sheet["Country Name"]
    from pygal.style import NeonStyle
    NeonStyle = NeonStyle(
    background='transparent',
    colors=('#FF0000', '#f1be54', '#76FC00', '#3280ee'),
    )
    line_chart = pygal.Line(fill=True, interpolate='cubic', style=NeonStyle, width=1000, x_label_rotation=90)
    line_chart.title = 'GNI (in USD)'
    line_chart.x_labels = map(str, range(1962, 2017))
    line_chart.value_formatter = lambda x: "%.2f" %x + "$"
    line_chart.add('China', gdp_sheet.loc["China"][6:61])
    line_chart.add('Thailand', gdp_sheet.loc["Thailand"][6:61])
    line_chart.add('Japan', gdp_sheet.loc["Japan"][6:61])
    line_chart.add('United States', gdp_sheet.loc["United States"][6:61])
    line_chart.render_to_file('Graph SVG/gni_line_chart.svg')
gni()
